# Generated by Django 4.2.2 on 2023-06-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_failed_attempt',
            field=models.DateTimeField(null=True),
        ),
    ]
