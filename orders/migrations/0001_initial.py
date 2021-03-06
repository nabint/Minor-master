# Generated by Django 3.1.6 on 2021-03-04 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fooditem', '0002_auto_20210223_1759'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('table_no', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooditem.fooditem', verbose_name='FOOD')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
