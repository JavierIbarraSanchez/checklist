# Generated by Django 4.0.2 on 2022-02-03 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='id_Checklist',
            new_name='id_checklist',
        ),
    ]
