# Generated by Django 5.2 on 2025-04-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_group_elements_element_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elements',
            old_name='element_group',
            new_name='group',
        ),
    ]
