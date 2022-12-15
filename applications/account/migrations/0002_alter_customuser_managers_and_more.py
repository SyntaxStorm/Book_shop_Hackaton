# Generated by Django 4.1.4 on 2022-12-15 19:27

import applications.account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', applications.account.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
