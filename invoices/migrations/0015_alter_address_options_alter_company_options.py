# Generated by Django 4.1.5 on 2023-06-26 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_address_alias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['alias']},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
    ]
