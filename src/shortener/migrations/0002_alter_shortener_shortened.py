# Generated by Django 3.2.12 on 2022-03-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='shortened',
            field=models.SlugField(unique=True),
        ),
    ]
