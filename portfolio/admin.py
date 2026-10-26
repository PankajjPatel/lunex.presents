from django.contrib import admin
from .models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'is_featured', 'is_concept',
        'display_order', 'created_date',
    )
    list_editable = ('is_featured', 'is_concept', 'display_order')
    list_filter = ('category', 'is_featured', 'is_concept')
    search_fields = ('title', 'short_description', 'client_name')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_deliverables_list',)
    fieldsets = (
        ('Project Info', {
            'fields': (
                'title', 'slug', 'category', 'client_name',
                'short_description', 'description', 'deliverables',
                'get_deliverables_list',
            ),
        }),
        ('Media', {
            'fields': ('thumbnail',),
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_concept', 'display_order', 'created_date'),
        }),
    )
