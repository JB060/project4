from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_lenght=200)
    quantity = models.IntergerField()
    category = models.ForeignKey('category', on_delete=models.SET_Null, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


class Category(models.Model):
    name = models.CharField(max_lenght=200)

    def __str__(self):
        return self.name 