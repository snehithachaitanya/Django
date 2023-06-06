# Generated by Django 4.1.7 on 2023-05-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0003_newsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='pompletDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('page', models.PositiveIntegerField()),
                ('fold', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]