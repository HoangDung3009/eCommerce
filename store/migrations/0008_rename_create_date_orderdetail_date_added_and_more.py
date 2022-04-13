# Generated by Django 4.0.3 on 2022-04-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_category_cat_thumb_alter_product_product_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='create_date',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='order',
            name='isCancelled',
        ),
        migrations.RemoveField(
            model_name='order',
            name='isPaid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ship_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_money',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='total_money',
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
