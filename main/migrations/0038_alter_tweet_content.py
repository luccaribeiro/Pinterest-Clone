# Generated by Django 4.0.6 on 2022-08-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_remove_retweet_original_tweet_remove_retweet_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
