# Generated by Django 2.0.6 on 2018-12-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaApp', '0004_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='requests',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
