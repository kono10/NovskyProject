from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Visual(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(help_text="should be javascript")
    description = models.TextField(blank=True, help_text="extended description giving additional info to the visual, similar to a blog post")
    detail = models.CharField(max_length=300, blank=True, help_text="short description specfic to the visual, ex: X axis represents ...")
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return self.name
