# Generated by Django 4.0.3 on 2022-04-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='customer'),
        ),
    ]
