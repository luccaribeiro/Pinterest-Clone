# Generated by Django 4.0.6 on 2022-07-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_like_user_alter_profile_nickname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reply', to='main.tweet'),
        ),
    ]