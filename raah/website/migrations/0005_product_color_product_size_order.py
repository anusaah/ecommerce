# Generated by Django 4.0.3 on 2022-03-31 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField(default=0)),
                ('order_date', models.DateField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
