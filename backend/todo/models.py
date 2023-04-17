"""
This module defines a Django model for a todo item with a
title, description, completion status, due date and priority level.
"""
from django.db import models
from django.forms import ValidationError


class Todo(models.Model):
    """
    A model representing a todo item with
    a title, description, completion status, due date and priority level.
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(
        choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)

    def __str__(self):
        """
        Returns a string representation which includes the title and priority level.
        """
        return f"{self.title} {self.get_priority_display()}"
    def clean(self):
        if len(self.title) < 5:
            raise ValidationError({'title': 'Title must be at least 5 characters long.'})
