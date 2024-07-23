# Generated by Django 5.0.6 on 2024-07-22 06:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='User',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('contact_me', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('payment_method', models.CharField(choices=[('Khalti', 'Khalti'), ('cash on Delivery', 'cash on Delivery'), ('Esewa', 'Esewa')], max_length=200)),
                ('payment_status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
