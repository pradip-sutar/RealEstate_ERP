# Generated by Django 5.0.6 on 2024-09-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roles_Rights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.JSONField(),
        ),
    ]