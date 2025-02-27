# Generated by Django 5.1.3 on 2025-01-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mymodel',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_auto_field', models.BigIntegerField()),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=255)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('float_field', models.FloatField()),
                ('generic_ip_address_field', models.GenericIPAddressField()),
            ],
        ),
    ]
