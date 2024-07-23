# Generated by Django 5.0.6 on 2024-07-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti')], max_length=200),
        ),
    ]
