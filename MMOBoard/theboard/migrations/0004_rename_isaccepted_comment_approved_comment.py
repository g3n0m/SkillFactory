# Generated by Django 4.0.1 on 2022-01-20 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theboard', '0003_alter_userprofile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='isAccepted',
            new_name='approved_comment',
        ),
    ]