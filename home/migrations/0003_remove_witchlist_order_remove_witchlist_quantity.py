# Generated by Django 4.0.1 on 2022-01-20 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_witchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='witchlist',
            name='order',
        ),
        migrations.RemoveField(
            model_name='witchlist',
            name='quantity',
        ),
    ]
