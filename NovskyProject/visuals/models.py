from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Visual(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(help_text="should be javascript")
    summary = models.TextField(blank=True)
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return self.name
