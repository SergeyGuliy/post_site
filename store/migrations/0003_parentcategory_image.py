# Generated by Django 2.2.1 on 2019-05-30 21:21

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to=store.models.image_folder),
        ),
    ]