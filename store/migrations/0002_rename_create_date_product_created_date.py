# Generated by Django 4.0.3 on 2022-04-04 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
