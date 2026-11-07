from django.contrib import admin
from .models import AuditScan, AuditFinding


class AuditFindingInline(admin.TabularInline):
    model = AuditFinding
    extra = 0
    fields = ('module', 'severity', 'title', 'risk_score', 'is_resolved')
    readonly_fields = ('module', 'severity', 'title', 'risk_score')


@admin.register(AuditScan)
class AuditScanAdmin(admin.ModelAdmin):
    list_display = (
        'domain',
        'company_name',
        'overall_score',
        'risk_level',
        'critical_count',
        'high_count',
        'status',
        'created_at',
    )
    list_filter = ('risk_level', 'status', 'ssl_valid', 'has_privacy_policy', 'has_cookie_banner')
    search_fields = ('domain', 'target_url', 'company_name', 'requester_email')
    inlines = [AuditFindingInline]
    ordering = ('-created_at',)


@admin.register(AuditFinding)
class AuditFindingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'audit',
        'module',
        'severity',
        'risk_score',
        'is_resolved',
        'created_at',
    )
    list_editable = ('is_resolved',)
    list_filter = ('module', 'severity', 'is_resolved', 'created_at')
    search_fields = ('title', 'description', 'evidence', 'recommended_fix', 'regulatory_reference')
    ordering = ('-created_at',)

