# Generated by Django 4.1 on 2022-09-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0009_alter_visual_viz_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="visual",
            name="viz_description",
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
