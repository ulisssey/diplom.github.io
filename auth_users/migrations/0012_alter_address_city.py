# Generated by Django 3.2.5 on 2022-05-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0011_alter_address_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
