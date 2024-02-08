# Generated by Django 5.0.1 on 2024-02-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_listing_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='snippet',
            field=models.CharField(max_length=50),
        ),
    ]
