# Generated by Django 5.0.3 on 2024-04-15 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xabar', '0002_alter_comment_muallif_alter_comment_news'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='muallif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muallif', to=settings.AUTH_USER_MODEL),
        ),
    ]
