
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MERCHANT = "MERCHANT", "Merchant"
        DISPATCHER = "DISPATCHER", "Dispatcher"
        COURIER = "COURIER", "Courier"
        WAREHOUSE_STAFF = "WAREHOUSE_STAFF", "Warehouse Staff"
        CUSTOMER = "CUSTOMER", "Customer"

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
