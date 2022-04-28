# Generated by Django 3.2.9 on 2021-11-02 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0011_alter_postcategory_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
