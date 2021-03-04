# Generated by Django 3.1.6 on 2021-03-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Served', 'Order is Served'), ('Cooking', 'Order is Cooking')], default='Served', max_length=30),
        ),
    ]