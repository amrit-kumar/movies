# Generated by Django 2.0.13 on 2019-04-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('popularity', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('imdb_score', models.FloatField(blank=True, default=None, null=True)),
                ('genre', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
