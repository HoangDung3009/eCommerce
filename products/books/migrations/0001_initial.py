# Generated by Django 4.0.3 on 2022-04-08 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0004_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=500, null=True)),
                ('author_email', models.CharField(blank=True, max_length=500, null=True)),
                ('author_phone', models.IntegerField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(blank=True, max_length=500, null=True)),
                ('publisher_email', models.IntegerField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.product')),
                ('publisher', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.author')),
            ],
            bases=('store.product',),
        ),
    ]