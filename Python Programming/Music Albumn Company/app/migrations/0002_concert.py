# Generated by Django 4.2.7 on 2024-04-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('awards', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
