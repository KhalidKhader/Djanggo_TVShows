# Generated by Django 4.1.7 on 2023-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Khalidapp', '0007_tvshows_user_alter_likes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshows',
            name='likeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='likeFlag',
            field=models.BooleanField(default=False),
        ),
    ]
