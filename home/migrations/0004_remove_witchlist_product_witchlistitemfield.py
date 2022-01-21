# Generated by Django 4.0.1 on 2022-01-20 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_witchlist_order_remove_witchlist_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='witchlist',
            name='product',
        ),
        migrations.CreateModel(
            name='WitchlistItemField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product')),
                ('witchlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.witchlist')),
            ],
        ),
    ]
