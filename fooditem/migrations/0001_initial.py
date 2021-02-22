# Generated by Django 3.1.6 on 2021-02-22 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('item_category', models.CharField(max_length=255)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
        ),
    ]