# Generated by Django 4.0.5 on 2022-06-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subscirbenow'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutusPage1st',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Abouts header-1')),
                ('abouts', models.TextField(verbose_name='About as-1')),
                ('img', models.ImageField(upload_to='media', verbose_name='BTravel image-1')),
            ],
            options={
                'verbose_name': 'AboutAsTeam-1',
                'verbose_name_plural': 'AboutsAsTeam-1',
            },
        ),
        migrations.CreateModel(
            name='AboutusPage2th',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Abouts header-2')),
                ('abouts', models.TextField(verbose_name='About as-2')),
                ('img', models.ImageField(upload_to='media', verbose_name='BTravel image-2')),
            ],
            options={
                'verbose_name': 'AboutAsTeam-2',
                'verbose_name_plural': 'AboutsAsTeam-2',
            },
        ),
        migrations.CreateModel(
            name='AboutusPage3th',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Abouts header-3')),
                ('abouts', models.TextField(verbose_name='About as-3')),
                ('img', models.ImageField(upload_to='media', verbose_name='BTravel image-3')),
            ],
            options={
                'verbose_name': 'AboutAsTeam-3',
                'verbose_name_plural': 'AboutsAsTeam-3',
            },
        ),
    ]
