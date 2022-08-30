from django.db import models


class VizType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VizResource(models.Model):
    """ resources use to cite and give credit """

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
    summary = models.TextField(blank=True)
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, related_name="tag")
    viz_resources = models.ForeignKey(
        VizResource, related_name="resource", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
