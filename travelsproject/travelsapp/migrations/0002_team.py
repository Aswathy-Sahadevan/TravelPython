# Generated by Django 4.1.7 on 2023-03-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='pics')),
                ('name1', models.CharField(max_length=250)),
                ('about', models.TextField()),
            ],
        ),
    ]
