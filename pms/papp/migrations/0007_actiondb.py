# Generated by Django 4.1.7 on 2023-05-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0006_rename_igid_instadb_ig'),
    ]

    operations = [
        migrations.CreateModel(
            name='actionDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('message', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
