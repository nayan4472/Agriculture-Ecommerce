# Generated by Django 4.2.3 on 2024-04-11 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0004_alter_cart_iid_alter_payment_iid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OnlinePayment',
        ),
    ]