# Generated by Django 2.2.1 on 2019-06-09 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20190609_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_total',
            new_name='cart_total_price',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='item_total',
            new_name='item_total_price',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]