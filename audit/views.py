import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import AuditScan, AuditFinding
from .engine import run_compliance_audit


def audit_home(request):
    """SaaS Landing Page: Know Your Compliance Risks Before They Become Expensive."""
    recent_scans = AuditScan.objects.filter(status='completed')[:5]
    total_audits = AuditScan.objects.count()
    context = {
        'page_title': 'AuditFlow — Privacy & Regulatory Compliance Audit Platform by Lunex Presents',
        'meta_description': 'Automated compliance monitoring, DPDP Act 2023 checks, cookie consent, session replay security, and RBI auto-debit audit platform for Indian tech businesses.',
        'recent_scans': recent_scans,
        'total_audits': total_audits,
    }
    return render(request, 'audit/home.html', context)


@require_POST
def start_scan(request):
    """Run an automated compliance audit scan on submitted URL."""
    url = request.POST.get('url', '').strip()
    company_name = request.POST.get('company_name', '').strip()
    email = request.POST.get('email', '').strip()

    if not url:
        return redirect('audit:home')

    scan = run_compliance_audit(url=url, company_name=company_name, email=email)
    return redirect('audit:report', scan_id=scan.id)


def audit_report(request, scan_id):
    """Interactive compliance audit report with score, risk distribution, and recommendations."""
    scan = get_object_or_404(AuditScan, id=scan_id)
    findings = scan.findings.all()

    module_filter = request.GET.get('module', 'all')
    severity_filter = request.GET.get('severity', 'all')

    if module_filter != 'all':
        findings = findings.filter(module=module_filter)
    if severity_filter != 'all':
        findings = findings.filter(severity=severity_filter)

    resolved_count = scan.findings.filter(is_resolved=True).count()
    total_findings = scan.findings.count()
    unresolved_count = total_findings - resolved_count

    context = {
        'scan': scan,
        'findings': findings,
        'all_findings_count': total_findings,
        'resolved_count': resolved_count,
        'unresolved_count': unresolved_count,
        'selected_module': module_filter,
        'selected_severity': severity_filter,
        'page_title': f'Compliance Audit Report — {scan.domain or scan.company_name} | Lunex Presents',
        'meta_description': f'Detailed privacy and security compliance audit findings for {scan.domain}.',
    }
    return render(request, 'audit/report.html', context)


def audit_dashboard(request):
    """Central compliance monitoring dashboard."""
    scans = AuditScan.objects.all()[:20]
    total_audits = AuditScan.objects.count()
    critical_total = AuditFinding.objects.filter(severity='critical', is_resolved=False).count()
    high_total = AuditFinding.objects.filter(severity='high', is_resolved=False).count()
    resolved_total = AuditFinding.objects.filter(is_resolved=True).count()

    context = {
        'scans': scans,
        'total_audits': total_audits,
        'critical_total': critical_total,
        'high_total': high_total,
        'resolved_total': resolved_total,
        'page_title': 'Compliance Operations Dashboard — Lunex Presents',
        'meta_description': 'Real-time overview of compliance scores, security findings, and remediation status.',
    }
    return render(request, 'audit/dashboard.html', context)


@require_POST
def toggle_resolution(request, finding_id):
    """Toggle finding resolution status via AJAX."""
    finding = get_object_or_404(AuditFinding, id=finding_id)
    finding.is_resolved = not finding.is_resolved
    if finding.is_resolved:
        finding.resolved_at = timezone.now()
    else:
        finding.resolved_at = None
    finding.save()

    finding.audit.recalculate_score()

    return JsonResponse({
        'success': True,
        'is_resolved': finding.is_resolved,
        'new_score': finding.audit.overall_score,
        'risk_level': finding.audit.risk_level,
        'critical_count': finding.audit.critical_count,
        'high_count': finding.audit.high_count,
    })
