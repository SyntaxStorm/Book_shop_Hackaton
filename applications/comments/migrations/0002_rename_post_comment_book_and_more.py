# Generated by Django 4.1.4 on 2022-12-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='commentary',
        ),
    ]