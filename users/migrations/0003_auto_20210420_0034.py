# Generated by Django 2.2.5 on 2021-04-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210306_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avartar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
