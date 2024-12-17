from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem

class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user.

    Inherits from Django's UserCreationForm and adds an email field.
    
    Attributes:
    - email (EmailField): The email address of the user.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
    """
    Form for creating or updating an inventory item.

    Allows users to enter details for an inventory item including name, quantity, and category.

    Attributes:
    - category (ModelChoiceField): A dropdown to select a category for the inventory item, populated with all categories.
    """
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)

    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category']
