# Generated by Django 4.2.2 on 2023-06-18 17:24

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0008_alter_applicant_company_alter_interview_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Resume',
            field=models.FileField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='raw/'),
        ),
    ]
