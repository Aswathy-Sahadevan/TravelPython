# Generated by Django 4.1.7 on 2023-03-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0004_alter_team_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img1',
            field=models.ImageField(upload_to='pics image'),
        ),
    ]
