# Generated by Django 4.0.1 on 2022-02-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_creation', '0002_remove_usercreation_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreation',
            name='date_of_birth',
        ),
    ]
