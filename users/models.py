from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('admin', 'Admin'),
        ('company', 'Company'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=USER_ROLES, default='customer')

    def __str__(self):
        return f"{self.username} ({self.role})"

