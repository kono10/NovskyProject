# Generated by Django 4.1 on 2022-09-24 19:01

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0013_alter_visual_summary_alter_visual_viz_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visual",
            name="summary",
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
