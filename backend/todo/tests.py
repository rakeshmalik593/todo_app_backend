"""
Module that defines the Todo model and its tests.
The Todo model represents a single todo item with
a title, description, priority, due date, and a completed flag.
This module also contains tests for the Todo model.
"""
from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    """Test case for the Todo model."""
    @classmethod
    def setUpTestData(cls):
        """Set up a test todo object for testing."""
        Todo.objects.create(title='Test Todo', description='This is a test todo',
        due_date=date.today())
    def test_title_max_length(self):
        """Test that the title field has a max length of 120 characters."""
        todo = Todo.objects.get(id=1)
        max_length = todo._meta.get_field('title').max_length
        self.assertEqual(max_length, 120)
    def test_priority_choices(self):
        """Test that the priority field has the correct choices."""
        todo = Todo.objects.get(id=1)
        choices = todo._meta.get_field('priority').choices
        self.assertEqual(choices, [(1, 'Low'), (2, 'Medium'), (3, 'High')])

    def test_todo_completed_default(self):
        """Test that the completed field defaults to False."""
        todo = Todo.objects.get(id=1)
        self.assertFalse(todo.completed)
    def test_todo_string_representation(self):
        """Test that the todo object is represented as expected as a string."""
        todo = Todo.objects.get(id=1)
        expected_title = todo.title
        expected_priority = todo.get_priority_display()
        self.assertEqual(str(todo), f"{expected_title} {expected_priority}")
    def test_todo_title_min_length(self):
        """Test that the title field must be at least 5 characters long."""
        todo = Todo.objects.create(title='t',description='abcefgh', priority=2)
        with self.assertRaises(ValidationError) as validation_error:
            todo.full_clean()
        error_message = validation_error.exception.message_dict.get('title')[0]
        self.assertEqual(error_message, 'Title must be at least 5 characters long.')
    def test_todo_title_valid_length(self):
        """Test that a valid title length of 5 characters passes validation."""
        todo = Todo.objects.get(id=1)
        todo.title = '12345'
        todo.full_clean()
        self.assertEqual(todo.title, '12345')
