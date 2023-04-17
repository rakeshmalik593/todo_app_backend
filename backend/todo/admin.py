"""
This module registers the Todo model with the Django admin interface and defines a custom ModelAdmin class.

The TodoAdmin class specifies which fields should be displayed in admin interface.
"""

from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """
    A custom ModelAdmin class for the Todo model
    """
    list_display = ('title', 'description',
                    'completed', 'due_date', 'priority')


# Register the Todo model with the TodoAdmin configuration class.
admin.site.register(Todo, TodoAdmin)
