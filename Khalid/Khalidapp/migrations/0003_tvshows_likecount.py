# Generated by Django 4.1.7 on 2023-03-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Khalidapp', '0002_tvshows'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshows',
            name='likeCount',
            field=models.IntegerField(null=True),
        ),
    ]
