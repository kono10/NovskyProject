from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Visual(models.Model):
    visual_name = models.CharField(max_length=100)
    visual_body = models.TextField()
    description = models.TextField()
    detail = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return self.visual_name
