from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'service_interest', 'created_at', 'is_read',
    )
    list_editable = ('is_read',)
    list_filter = ('service_interest', 'is_read')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'service_interest', 'message', 'created_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        # Enquiries are created only through the contact form, not manually.
        return False
