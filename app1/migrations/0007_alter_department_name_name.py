# Generated by Django 5.0.6 on 2024-06-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_preprojectnew_generate_agreement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_name',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]