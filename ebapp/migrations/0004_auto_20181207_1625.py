# Generated by Django 2.1.2 on 2018-12-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebapp', '0003_auto_20181207_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_gender',
            field=models.CharField(max_length=20),
        ),
    ]