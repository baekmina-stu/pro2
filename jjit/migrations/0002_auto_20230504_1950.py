# Generated by Django 3.1.3 on 2023-05-04 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jjit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
