# Generated by Django 3.2.9 on 2023-10-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user'), ('waiter', 'waiter')], default='user', max_length=15),
        ),
    ]
