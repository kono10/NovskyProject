# Generated by Django 4.1 on 2022-08-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visuals", "0002_alter_visual_tags"),
    ]

    operations = [
        migrations.RenameField(
            model_name="visual", old_name="visual_name", new_name="name",
        ),
        migrations.RemoveField(model_name="visual", name="visual_body",),
        migrations.AddField(
            model_name="visual",
            name="body",
            field=models.TextField(default="foo", help_text="should be javascript"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="visual",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="extended description giving additional info to the visual, similar to a blog post",
            ),
        ),
        migrations.AlterField(
            model_name="visual",
            name="detail",
            field=models.CharField(
                blank=True,
                help_text="short description specfic to the visual, ex: X axis represents ...",
                max_length=300,
            ),
        ),
    ]
