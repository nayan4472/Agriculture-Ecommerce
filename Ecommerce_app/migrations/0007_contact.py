# Generated by Django 4.2.3 on 2024-04-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0006_onlinepayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('con_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
