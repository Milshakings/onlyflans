# Generated by Django 5.0.6 on 2024-07-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_flan_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='image',
            field=models.ImageField(null=True, upload_to='flanes/'),
        ),
    ]
