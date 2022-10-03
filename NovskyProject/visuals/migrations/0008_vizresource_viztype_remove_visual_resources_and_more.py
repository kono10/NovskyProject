# Generated by Django 4.0.5 on 2022-08-29 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0007_remove_visual_viz_type_alter_resource_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VizResource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=400)),
                ("description", models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="VizType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="visual",
            name="resources",
        ),
        migrations.DeleteModel(
            name="Resource",
        ),
        migrations.AddField(
            model_name="visual",
            name="viz_resources",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resource",
                to="visuals.vizresource",
            ),
        ),
        migrations.AddField(
            model_name="visual",
            name="viz_type",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="type",
                to="visuals.viztype",
            ),
        ),
    ]
