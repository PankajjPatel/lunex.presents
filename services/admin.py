from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'starting_price', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'short_description', 'full_description', 'ideal_for')
    list_filter = ('is_active',)
