# Generated by Django 2.1.7 on 2019-02-17 09:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0006_auto_20190217_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneno',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]
