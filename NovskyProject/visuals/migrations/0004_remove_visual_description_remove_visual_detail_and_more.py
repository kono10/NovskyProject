# Generated by Django 4.1 on 2022-08-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0003_rename_visual_name_visual_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="visual", name="description",),
        migrations.RemoveField(model_name="visual", name="detail",),
        migrations.AddField(
            model_name="visual", name="summary", field=models.TextField(blank=True),
        ),
    ]
