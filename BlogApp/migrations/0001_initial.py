# Generated by Django 3.0.5 on 2021-10-06 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(upload_to='media')),
                ('tag', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2021, 10, 6, 10, 19, 14, 223804))),
            ],
        ),
    ]
