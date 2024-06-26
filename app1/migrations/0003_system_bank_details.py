# Generated by Django 5.0.6 on 2024-06-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_system_branch_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='System_bank_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('IFSC', models.CharField(max_length=11)),
                ('account_name', models.CharField(max_length=255)),
                ('account_no', models.CharField(max_length=20)),
                ('bank_logo', models.ImageField(blank=True, null=True, upload_to='bank_logos/')),
                ('account_type', models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current'), ('Fixed Deposit', 'Fixed Deposit'), ('Recurring Deposit', 'Recurring Deposit'), ('NRO', 'NRO'), ('NRE', 'NRE'), ('FCNR', 'FCNR')], max_length=50)),
            ],
        ),
    ]
