# Generated by Django 4.0.5 on 2022-06-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_blogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageToSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='turs name')),
                ('about', models.CharField(max_length=250, verbose_name='About next travel')),
                ('img', models.ImageField(upload_to='media', verbose_name='turs image')),
            ],
            options={
                'verbose_name': 'ToSupport',
                'verbose_name_plural': 'ToSupports',
            },
        ),
    ]
