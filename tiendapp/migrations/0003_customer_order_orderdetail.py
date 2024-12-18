# Generated by Django 5.1.4 on 2024-12-12 23:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendapp', '0002_category_productcategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.TextField()),
                ('shipping_address', models.TextField()),
                ('phone', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.TextField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=32)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tiendapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tiendapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tiendapp.product')),
            ],
        ),
    ]