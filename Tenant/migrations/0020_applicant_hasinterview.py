# Generated by Django 4.2.2 on 2023-06-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0019_alter_interview_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='hasInterview',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
