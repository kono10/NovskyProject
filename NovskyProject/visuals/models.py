from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


class VizType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VizResource(models.Model):
    """resources use to cite and give credit"""

    name = models.CharField(max_length=100)
    url = models.URLField(max_length=400)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Visual(models.Model):
    name = models.CharField(max_length=100)
    viz_type = models.ForeignKey(
        VizType, related_name="type", on_delete=models.CASCADE, null=True, blank=True
    )
    body = models.TextField(help_text="should be javascript or html")
    summary = MarkdownxField(blank=True)
    viz_description = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="help explain the viz iteself, ie x axis represents ...",
    )
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, related_name="tag")
    viz_resources = models.ForeignKey(
        VizResource,
        related_name="resource",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @property
    def formatted_markdown(self):
        return markdownify(self.summary)

    def __str__(self):
        return self.name

    @property
    def viz_json(self) -> str:
        return json.loads(self.body)

    @property
    def background_color(self):
        try:
            if self.viz_type.name.upper() == "ALTAIR":
                return self.viz_json.get("config").get("background")
            if self.viz_type.name.upper() == "PLOTLY":
                return (
                    self.viz_json.get("data")[2].get("cells").get("fill").get("color")
                )
        except Exception as e:
            default_color = "grey"
            logger.warning(
                f"{self.viz_type} viz background defaulting to {default_color} - Error: {e}"
            )
            return "grey"

    @property
    def font_color(self):
        try:
            if self.viz_type.name.upper() == "ALTAIR":
                return self.viz_json.get("config").get("title").get("color")
            if self.viz_type.name.upper() == "PLOTLY":
                return (
                    self.viz_json.get("data")[0].get("cells").get("font").get("color")
                )
        except Exception as e:
            default_color = "white"
            logger.warning(
                f"{self.viz_type} viz font color defaulting to {default_color} - Error: {e}"
            )
            return default_color
