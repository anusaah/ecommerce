# Generated by Django 4.0.3 on 2022-04-16 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0015_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='cart_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.cart'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]