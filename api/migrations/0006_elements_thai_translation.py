# Generated by Django 5.2 on 2025-04-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_element_group_elements_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='elements',
            name='thai_translation',
            field=models.CharField(default=255, max_length=255),
        ),
    ]
