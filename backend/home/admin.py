from django.contrib import admin
from .models import EmergencyContact, UserProfile

admin.site.register(UserProfile)
admin.site.register(EmergencyContact)

# Register your models here.
