from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Your custom fields (if any)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Resolves the conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Resolves the conflict
        blank=True
    )
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name