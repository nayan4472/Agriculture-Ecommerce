# Generated by Django 4.2.3 on 2024-04-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0003_alter_onlinepayment_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='iid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='iid',
            field=models.IntegerField(),
        ),
    ]
