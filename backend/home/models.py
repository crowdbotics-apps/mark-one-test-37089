from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    "Generated Model"
    telephone = models.BigIntegerField()
    occupation = models.CharField(
        max_length=256,
    )
    profile_picture = models.CharField(
        max_length=256,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="userprofile_user",
    )


class EmergencyContact(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="emergencycontact_user",
    )
    email = models.EmailField(
        max_length=254,
    )
    phone_number = models.PositiveIntegerField()
