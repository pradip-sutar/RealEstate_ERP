# Generated by Django 5.0.6 on 2024-07-25 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mob', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('present_address', models.TextField()),
                ('present_city', models.CharField(max_length=255)),
                ('present_district', models.CharField(max_length=255)),
                ('present_country', models.CharField(max_length=255)),
                ('present_pincode', models.CharField(max_length=10)),
                ('permanent_address', models.TextField()),
                ('permanent_city', models.CharField(max_length=255)),
                ('permanent_district', models.CharField(max_length=255)),
                ('permanent_country', models.CharField(max_length=255)),
                ('permanent_pincode', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=255)),
                ('religion', models.CharField(max_length=255)),
                ('caste', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead_Enquiry_Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead_Enquiry_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_status', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('comm_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enquiry_Bucket.communication_type')),
            ],
        ),
    ]