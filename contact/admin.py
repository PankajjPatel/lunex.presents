from django.contrib import admin
from .models import Enquiry, Review


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'enquiry_type',
        'business_name',
        'email',
        'phone',
        'service_interest',
        'website_type',
        'budget_range',
        'created_at',
        'is_read',
    )
    list_editable = ('is_read',)
    list_filter = ('enquiry_type', 'service_interest', 'website_type', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'business_name', 'phone', 'message', 'expected_features')
    readonly_fields = (
        'enquiry_type', 'name', 'email', 'phone', 'business_name',
        'service_interest', 'website_type', 'expected_features',
        'budget_range', 'message', 'created_at'
    )
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'business_name',
        'rating',
        'is_verified_client',
        'is_approved',
        'created_at',
    )
    list_editable = ('is_approved', 'is_verified_client')
    list_filter = ('is_approved', 'is_verified_client', 'rating', 'created_at')
    search_fields = ('client_name', 'business_name', 'project_title', 'feedback')
    actions = ['approve_reviews', 'reject_reviews', 'verify_clients']

    @admin.action(description="Approve selected reviews for public display")
    def approve_reviews(self, request, queryset):
        count = queryset.update(is_approved=True)
        self.message_user(request, f"{count} review(s) approved and published.")

    @admin.action(description="Reject selected reviews (hide from public)")
    def reject_reviews(self, request, queryset):
        count = queryset.update(is_approved=False)
        self.message_user(request, f"{count} review(s) unpublished/rejected.")

    @admin.action(description="Mark selected reviewers as Verified Clients")
    def verify_clients(self, request, queryset):
        count = queryset.update(is_verified_client=True)
        self.message_user(request, f"{count} review(s) marked as verified client.")
