# Generated by Django 4.2.2 on 2023-06-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0003_alter_subscription_name_alter_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]