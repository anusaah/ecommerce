# Generated by Django 4.0.3 on 2022-03-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_product_category_product_image_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phno', models.IntegerField()),
            ],
        ),
    ]
