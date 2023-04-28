# Generated by Django 2.2.28 on 2023-04-28 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_delete_emergencycontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('detail', models.CharField(max_length=256)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]