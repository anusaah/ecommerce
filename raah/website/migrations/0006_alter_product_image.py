# Generated by Django 4.0.3 on 2022-03-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product_color_product_size_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
