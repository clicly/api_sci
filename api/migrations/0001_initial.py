# Generated by Django 4.1.3 on 2023-02-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Environment')),
                ('capacity', models.IntegerField(verbose_name='Capacity of environment')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('available', models.BooleanField(verbose_name='Available')),
                ('description', models.TextField(verbose_name='Description of environment')),
                ('created_by', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_by', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Environment',
                'verbose_name_plural': 'Environments',
                'ordering': ['available', 'address', 'description'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=15, unique=True, verbose_name='CPF by responsable person')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Use Fee')),
                ('real_value_pay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('capacity', models.IntegerField()),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(verbose_name='Are you ready for do the booking?')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.environment', verbose_name='Environment')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
