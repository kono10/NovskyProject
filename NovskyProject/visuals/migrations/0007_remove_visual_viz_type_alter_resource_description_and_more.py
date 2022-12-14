# Generated by Django 4.0.5 on 2022-08-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0006_alter_resource_description_alter_resource_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="visual", name="viz_type",),
        migrations.AlterField(
            model_name="resource",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="visual",
            name="resources",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resource",
                to="visuals.resource",
            ),
        ),
    ]
