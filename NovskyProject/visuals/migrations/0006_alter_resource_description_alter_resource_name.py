# Generated by Django 4.0.5 on 2022-08-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0005_resource_visual_viz_type_alter_visual_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="description",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="resource", name="name", field=models.CharField(max_length=100),
        ),
    ]
