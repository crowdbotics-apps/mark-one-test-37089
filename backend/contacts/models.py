from django.conf import settings
from django.db import models


class Contacts(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contacts_user",
    )
    email = models.EmailField(
        max_length=254,
    )
    phone_number = models.CharField(
        max_length=256,
    )


# Create your models here.
