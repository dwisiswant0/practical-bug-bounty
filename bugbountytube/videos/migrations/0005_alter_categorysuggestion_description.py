# Generated by Django 4.1.6 on 2023-10-06 21:21

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_videosuggestion_categorysuggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorysuggestion',
            name='description',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
