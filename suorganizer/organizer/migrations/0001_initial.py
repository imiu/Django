# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    #        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=31)),
                ('pub_date', models.DateField()),
                ('link', models.URLField(max_length=255, verbose_name=b'Date Published')),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
                'verbose_name': 'news article',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=31, db_index=True)),
                ('slug', models.SlugField(help_text=b'A label for URL config', unique=True, max_length=31)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name=b'Date Founded')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=31)),
                ('slug', models.SlugField(help_text=b'A label for URL config.', unique=True, max_length=31)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(to='organizer.Startup'),
        ),
    ]
