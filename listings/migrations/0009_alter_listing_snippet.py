# Generated by Django 5.0.1 on 2024-02-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='snippet',
            field=models.CharField(default='Click link above to know more about the business!!!', max_length=50),
        ),
    ]