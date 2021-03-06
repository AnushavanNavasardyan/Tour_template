# Generated by Django 4.0.5 on 2022-06-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NextTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Next travel name')),
                ('about', models.CharField(max_length=50, verbose_name='About next travel')),
                ('img', models.ImageField(upload_to='media', verbose_name='BTravel image')),
            ],
            options={
                'verbose_name': 'Travel',
                'verbose_name_plural': 'Travels',
            },
        ),
    ]
