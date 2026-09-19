from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "technologies",
    )

    list_editable = (
        "is_featured",
    )

    readonly_fields = (
        "created_at",
    )