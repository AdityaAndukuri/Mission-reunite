# Generated by Django 2.1.2 on 2018-11-04 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0014_case_confimred_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='confimred_status',
            new_name='confirmed_status',
        ),
    ]