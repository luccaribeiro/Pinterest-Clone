# Generated by Django 4.0.6 on 2022-07-18 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_comentarios_options_comentarios_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tweet'),
        ),
    ]