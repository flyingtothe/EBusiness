# Generated by Django 2.1.2 on 2018-12-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_password',
            field=models.CharField(max_length=100),
        ),
    ]
