# Generated by Django 4.1.4 on 2022-12-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.PositiveSmallIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')], help_text='max 5 stars'),
        ),
    ]
