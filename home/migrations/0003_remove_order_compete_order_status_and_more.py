# Generated by Django 4.0.1 on 2022-01-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_address_customer_image_customer_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='compete',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PROSSED', 'process'), ('SHIPING', 'shiping'), ('ONTHEWAY', 'ontheway'), ('PROSSED', 'receved')], default=False, max_length=9),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default=(('PROSSED', 'process'),), upload_to='static/img/profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/img/project/'),
        ),
    ]
