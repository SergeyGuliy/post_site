# Generated by Django 2.2.1 on 2019-06-25 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20190624_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='store.Cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Оплачен', 'Оплачен'), ('Выполняется', 'Выполняется'), ('Выполнен', 'Выполнен')], default='Принят в обработку', max_length=100),
        ),
    ]