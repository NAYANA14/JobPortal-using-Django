# Generated by Django 4.0.1 on 2022-03-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='Interview_Date',
            field=models.DateField(null=True),
        ),
    ]