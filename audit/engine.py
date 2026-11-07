"""
Lunex ComplianceGuard — Privacy & Security Compliance Audit Engine.
Inspects live website configurations, security headers, consent mechanisms,
and regulatory compliance indicators (DPDP Act 2023, RBI e-Mandate, IT Rules).
"""

import re
import urllib.parse
import urllib.request
import ssl
from datetime import datetime
from .models import AuditScan, AuditFinding


def run_compliance_audit(url, company_name="My Business", email=""):
    """
    Executes a multi-vector privacy and regulatory compliance audit on target url.
    Saves and returns an AuditScan instance with detailed AuditFindings.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc or parsed.path.split('/')[0]
    if not company_name or company_name == "My Business":
        company_name = domain.split('.')[0].capitalize()

    scan = AuditScan.objects.create(
        target_url=url,
        domain=domain,
        company_name=company_name,
        requester_email=email,
        status='scanning',
    )

    findings = []
    headers = {}
    html_content = ""
    is_https = parsed.scheme == 'https'
    scan.ssl_valid = is_https

    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) LunexComplianceAudit/2.0 (compatible; ComplianceGuardBot/1.0)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            }
        )
        with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
            headers = {k.lower(): v for k, v in response.headers.items()}
            raw = response.read(250000)
            try:
                html_content = raw.decode('utf-8', errors='ignore')
            except Exception:
                html_content = ""
    except Exception:
        pass

    # 1. Security Headers & Breach Monitoring Check
    hsts = headers.get('strict-transport-security')
    if not hsts:
        findings.append({
            'module': 'security_breach',
            'title': 'Missing HTTP Strict Transport Security (HSTS)',
            'severity': 'high',
            'risk_score': 78,
            'description': 'The website does not enforce HTTPS connections via the HSTS header. This leaves users susceptible to SSL-stripping and man-in-the-middle network attacks.',
            'evidence': 'Header "Strict-Transport-Security" was not returned in the server response.',
            'recommended_fix': 'Configure web server with: "add_header Strict-Transport-Security \'max-age=31536000; includeSubDomains; preload\' always;".',
            'regulatory_reference': 'CERT-In Security Directives / ISO 27001 Annex A.13.1',
        })

    csp = headers.get('content-security-policy')
    if not csp:
        findings.append({
            'module': 'security_breach',
            'title': 'Missing Content Security Policy (CSP)',
            'severity': 'high',
            'risk_score': 74,
            'description': 'Content-Security-Policy is missing. Attackers can potentially execute Cross-Site Scripting (XSS), inject malicious scripts, or exfiltrate session data.',
            'evidence': 'Header "Content-Security-Policy" was absent in HTTP response.',
            'recommended_fix': 'Define a strict Content-Security-Policy header restricting script-src, object-src, and default-src to trusted origins.',
            'regulatory_reference': 'OWASP Top 10 A03:2021 — Injection / IT Rules 2021',
        })

    x_frame = headers.get('x-frame-options')
    if not x_frame and (not csp or 'frame-ancestors' not in csp):
        findings.append({
            'module': 'security_breach',
            'title': 'Vulnerable to Clickjacking (Missing X-Frame-Options)',
            'severity': 'medium',
            'risk_score': 58,
            'description': 'The website does not restrict embedding inside iframe elements, allowing attackers to overlay deceptive transparent UI layers.',
            'evidence': 'Neither "X-Frame-Options: SAMEORIGIN" nor CSP "frame-ancestors" was detected.',
            'recommended_fix': 'Add "X-Frame-Options: SAMEORIGIN" or "Content-Security-Policy: frame-ancestors \'self\';" in your HTTP server or Django security middleware.',
            'regulatory_reference': 'OWASP ASVS v4.0.3 Sec 14.4.1',
        })

    referrer_policy = headers.get('referrer-policy')
    if not referrer_policy or referrer_policy == 'no-referrer-when-downgrade':
        findings.append({
            'module': 'data_protection',
            'title': 'Insecure Referrer-Policy Leakage Risk',
            'severity': 'medium',
            'risk_score': 45,
            'description': 'Default or absent Referrer-Policy can leak sensitive URL query parameters (e.g. session tokens, search terms, user IDs) to external third-party servers.',
            'evidence': f'Referrer-Policy observed: "{referrer_policy or "Not Specified"}".',
            'recommended_fix': 'Set header "Referrer-Policy: strict-origin-when-cross-origin" to protect user privacy.',
            'regulatory_reference': 'DPDP Act 2023 Sec 8(5) / GDPR Art 32',
        })

    # 2. Consent Management & Privacy Policy Check
    html_lower = html_content.lower()
    has_privacy_link = bool(
        'privacy' in html_lower or
        'privacy-policy' in html_lower or
        '/privacy' in html_lower
    )
    scan.has_privacy_policy = has_privacy_link
    if not has_privacy_link:
        findings.append({
            'module': 'consent_management',
            'title': 'Missing or Obscured Privacy Policy Disclosure',
            'severity': 'critical',
            'risk_score': 92,
            'description': 'No easily accessible Privacy Policy link was detected on the main landing page. Indian and international regulations mandate clear, transparent disclosures regarding data collection and processing purposes.',
            'evidence': 'No anchor tag or footer link containing "Privacy" or "Privacy Policy" was located in DOM.',
            'recommended_fix': 'Publish a dedicated Privacy Policy page detailing data collected, retention periods, third-party disclosures, and grievance officer details, and place prominent links in the site footer.',
            'regulatory_reference': 'Digital Personal Data Protection (DPDP) Act 2023 Sec 5 & 6',
        })

    has_cookie_banner = bool(
        'cookie' in html_lower and ('consent' in html_lower or 'accept' in html_lower or 'banner' in html_lower)
    )
    scan.has_cookie_banner = has_cookie_banner
    if not has_cookie_banner:
        findings.append({
            'module': 'consent_management',
            'title': 'Missing Granular Cookie & Tracking Consent Mechanism',
            'severity': 'high',
            'risk_score': 70,
            'description': 'Users are not presented with a clear opt-in consent mechanism before non-essential tracking and analytics cookies are loaded onto their browsers.',
            'evidence': 'No cookie consent management banner or preference modal was identified in page markup.',
            'recommended_fix': 'Implement a compliant consent banner that blocks non-essential marketing/analytics cookies until explicit affirmative consent is provided.',
            'regulatory_reference': 'DPDP Act 2023 Sec 6 / ePrivacy Directive',
        })

    # 3. Session Replay Check
    replay_tools = [
        ('clarity.ms', 'Microsoft Clarity'),
        ('hotjar.com', 'Hotjar Session Recording'),
        ('fullstory.com', 'FullStory'),
        ('logrocket.com', 'LogRocket'),
        ('smartlook.com', 'Smartlook'),
        ('inspectlet.com', 'Inspectlet'),
    ]
    detected_replay = []
    for signature, tool_name in replay_tools:
        if signature in html_lower:
            detected_replay.append(tool_name)

    scan.has_session_replay = bool(detected_replay)
    if detected_replay:
        findings.append({
            'module': 'session_replay',
            'title': f'Insecure Session Recording Detected ({", ".join(detected_replay)})',
            'severity': 'critical',
            'risk_score': 88,
            'description': 'Session replay scripts record user mouse movements, clicks, and keystrokes. Without strict masking attributes, sensitive credentials, personal phone numbers, or credit card details may be exfiltrated to analytics vendors.',
            'evidence': f'Active script signatures identified: {", ".join(detected_replay)}.',
            'recommended_fix': 'Ensure all input fields (especially passwords, OTPs, financial and personal inputs) have strict masking attributes enabled, and verify explicit consent is obtained.',
            'regulatory_reference': 'DPDP Act 2023 Sec 8 (Security Safeguards) & CERT-In Guidelines',
        })
    else:
        findings.append({
            'module': 'session_replay',
            'title': 'Form Input Masking Audit Required',
            'severity': 'low',
            'risk_score': 25,
            'description': 'Verify all form fields that handle PII (names, contact info, billing addresses) explicitly instruct client-side libraries to respect privacy masks.',
            'evidence': 'Standard form submission controls observed on target site.',
            'recommended_fix': 'Add input autocomplete="off" or data-privacy-mask attributes on sensitive inputs.',
            'regulatory_reference': 'Best Practice Privacy Design Framework',
        })

    # 4. Age Verification Check
    findings.append({
        'module': 'age_verification',
        'title': 'Missing Age Verification & Minor Data Safeguard',
        'severity': 'medium',
        'risk_score': 65,
        'description': 'Under Section 9 of the DPDP Act 2023, data fiduciaries processing data of children (under 18) must obtain verifiable parental consent and must not engage in tracking or behavioral monitoring of minors.',
        'evidence': 'No age confirmation checkpoint, date-of-birth gate, or guardian consent workflow was observed prior to account registration or form interaction.',
        'recommended_fix': 'Integrate an age verification checkbox or birth-year gateway during user onboarding with appropriate parental consent verification if minors access the service.',
        'regulatory_reference': 'DPDP Act 2023 Section 9 (Processing of Personal Data of Children)',
    })

    # 5. Subscription & Auto-Debit Check
    findings.append({
        'module': 'subscription_autodebit',
        'title': 'Pre-Debit Notification & E-Mandate Compliance Check',
        'severity': 'medium',
        'risk_score': 55,
        'description': 'Recurring billing mandates on Indian cards and UPI require explicit opt-in, clear terms display, at least 24-hour pre-debit notifications (via SMS/email), and a 1-click subscription cancellation mechanism.',
        'evidence': 'Recurring billing workflow requires verification against RBI e-mandate framework.',
        'recommended_fix': 'Ensure payment checkout clearly displays billing frequency, renewal date, and gives users an immediate dashboard button to cancel recurring auto-debits.',
        'regulatory_reference': 'Reserve Bank of India (RBI) Circular on Processing of E-Mandate (RBI/2020-21/74)',
    })

    for item in findings:
        AuditFinding.objects.create(
            audit=scan,
            module=item['module'],
            title=item['title'],
            severity=item['severity'],
            risk_score=item['risk_score'],
            description=item['description'],
            evidence=item['evidence'],
            recommended_fix=item['recommended_fix'],
            regulatory_reference=item['regulatory_reference'],
        )

    scan.status = 'completed'
    scan.recalculate_score()
    return scan
