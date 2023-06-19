# Generated by Django 4.2.2 on 2023-06-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0006_subscription_users_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(choices=[('Bootstrap', 'Bootstrap'), ('Startup', 'Startup'), ('Business', 'Business')]),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='type',
            field=models.CharField(choices=[('Annually', 'Annually'), ('Monthly', 'Monthly')]),
        ),
    ]