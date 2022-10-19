# Generated by Django 2.0 on 2019-07-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parkingSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_no', models.CharField(max_length=20)),
                ('car_no', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('charged', models.BooleanField(default=False)),
                ('limit_reached', models.BooleanField(default=False)),
                ('limit', models.PositiveIntegerField(choices=[(1, '10 sec'), (2, '15 min'), (3, '20 min'), (4, '1 hour')], default=1)),
            ],
        ),
    ]