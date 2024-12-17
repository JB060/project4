from django.contrib import admin
from .models import InventoryItem, Category 

# Register the InventoryItem model to be managed through the Django admin interface
admin.site.register(InventoryItem)
"""
Registers the InventoryItem model with the Django admin site,
allowing it to be viewed and managed through the admin interface.
"""

# Register the Category model to be managed through the Django admin interface
admin.site.register(Category)
"""
Registers the Category model with the Django admin site,
enabling it to be accessed and managed in the admin interface.
"""

