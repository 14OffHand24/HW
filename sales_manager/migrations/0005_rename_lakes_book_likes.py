# Generated by Django 3.2.3 on 2021-05-22 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0004_book_lakes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='lakes',
            new_name='likes',
        ),
    ]
