import uuid
from django.db import models


SEVERITY_CHOICES = [
    ('critical', 'Critical Risk'),
    ('high', 'High Risk'),
    ('medium', 'Medium Risk'),
    ('low', 'Low Risk'),
]

MODULE_CHOICES = [
    ('age_verification', 'Age Verification & Parental Consent'),
    ('consent_management', 'Consent Management & Cookie Disclosures'),
    ('data_protection', 'Data Protection & PII Retention'),
    ('security_breach', 'Security Headers & Breach Monitoring'),
    ('session_replay', 'Session Replay & Insecure Analytics'),
    ('subscription_autodebit', 'Subscription & Auto-Debit Compliance'),
]


class AuditScan(models.Model):
    """A website/app compliance and privacy audit execution."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    target_url = models.URLField(max_length=255, verbose_name="Target Website URL")
    domain = models.CharField(max_length=150, blank=True)
    company_name = models.CharField(max_length=140, blank=True, default="My Business")
    requester_email = models.EmailField(blank=True)

    overall_score = models.PositiveSmallIntegerField(
        default=0,
        help_text="Compliance health score (0 to 100).",
    )
    risk_level = models.CharField(
        max_length=20,
        default='medium',
        choices=[
            ('critical', 'Critical Risk Exposure'),
            ('high', 'High Risk Exposure'),
            ('medium', 'Moderate Risk'),
            ('compliant', 'Generally Compliant'),
        ],
    )

    critical_count = models.PositiveSmallIntegerField(default=0)
    high_count = models.PositiveSmallIntegerField(default=0)
    medium_count = models.PositiveSmallIntegerField(default=0)
    low_count = models.PositiveSmallIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending Scan'),
            ('scanning', 'In Progress'),
            ('completed', 'Scan Completed'),
            ('failed', 'Scan Failed'),
        ],
        default='completed',
    )
    ssl_valid = models.BooleanField(default=True)
    has_privacy_policy = models.BooleanField(default=False)
    has_cookie_banner = models.BooleanField(default=False)
    has_session_replay = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Compliance Audit Scan'
        verbose_name_plural = 'Compliance Audit Scans'

    def __str__(self):
        return f"{self.domain or self.target_url} — Score: {self.overall_score}% ({self.created_at.strftime('%d %b %Y')})"

    def recalculate_score(self):
        """Recalculate overall score based on remaining unresolved findings."""
        unresolved = self.findings.filter(is_resolved=False)
        self.critical_count = unresolved.filter(severity='critical').count()
        self.high_count = unresolved.filter(severity='high').count()
        self.medium_count = unresolved.filter(severity='medium').count()
        self.low_count = unresolved.filter(severity='low').count()

        penalty = (
            (self.critical_count * 25) +
            (self.high_count * 15) +
            (self.medium_count * 8) +
            (self.low_count * 3)
        )
        self.overall_score = max(0, min(100, 100 - penalty))

        if self.critical_count > 0:
            self.risk_level = 'critical'
        elif self.high_count > 0:
            self.risk_level = 'high'
        elif self.overall_score >= 85:
            self.risk_level = 'compliant'
        else:
            self.risk_level = 'medium'

        self.save(update_fields=[
            'overall_score', 'risk_level',
            'critical_count', 'high_count', 'medium_count', 'low_count'
        ])


class AuditFinding(models.Model):
    """An individual compliance gap or vulnerability discovered during an audit."""

    audit = models.ForeignKey(
        AuditScan,
        on_delete=models.CASCADE,
        related_name='findings',
    )
    module = models.CharField(
        max_length=30,
        choices=MODULE_CHOICES,
        default='data_protection',
    )
    title = models.CharField(max_length=200)
    severity = models.CharField(
        max_length=15,
        choices=SEVERITY_CHOICES,
        default='medium',
    )
    risk_score = models.PositiveSmallIntegerField(
        default=50,
        help_text="Weighted risk score (0-100).",
    )
    description = models.TextField()
    evidence = models.TextField(
        blank=True,
        help_text="Observed headers, scripts, markup, or request patterns.",
    )
    recommended_fix = models.TextField(
        help_text="Actionable, step-by-step remediation recommendation.",
    )
    regulatory_reference = models.CharField(
        max_length=140,
        blank=True,
        help_text="e.g. 'DPDP Act 2023 Sec 9' or 'RBI E-Mandate Circular 2021'.",
    )
    is_resolved = models.BooleanField(
        default=False,
        help_text="Mark when user implements the suggested remediation.",
    )
    resolved_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(
        blank=True,
        help_text="Team notes or implementation comments.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            models.Case(
                models.When(severity='critical', then=models.Value(1)),
                models.When(severity='high', then=models.Value(2)),
                models.When(severity='medium', then=models.Value(3)),
                models.When(severity='low', then=models.Value(4)),
                default=models.Value(5),
                output_field=models.IntegerField(),
            ),
            '-created_at',
        ]
        verbose_name = 'Audit Finding'
        verbose_name_plural = 'Audit Findings'

    def __str__(self):
        return f"[{self.severity.upper()}] {self.title} ({self.get_module_display()})"

