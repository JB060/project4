from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    """
    Represents an item in the inventory.

    Attributes:
    - name (str): The name of the inventory item.
    - quantity (int): The number of items available in stock.
    - category (Category): A foreign key to the Category model that categorizes the item.
    - date_created (datetime): The date and time when the item was added to the inventory.
    - user (User): A foreign key to the User model representing the owner of the inventory item.
    """
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the InventoryItem object.

        Returns:
        - str: The name of the inventory item.
        """
        return self.name

class Category(models.Model):
    """
    Represents a category for grouping inventory items.

    Attributes:
    - name (str): The name of the category.
    """
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        Returns a string representation of the Category object.

        Returns:
        - str: The name of the category.
        """
        return self.name
