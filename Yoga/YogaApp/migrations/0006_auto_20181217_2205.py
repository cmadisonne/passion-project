# Generated by Django 2.0.6 on 2018-12-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaApp', '0005_auto_20181217_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]