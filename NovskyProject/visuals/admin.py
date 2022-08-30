from django.contrib import admin
from .models import Tag, Visual, VizResource, VizType

# Register your models here.
admin.site.register(Tag)
admin.site.register(Visual)
admin.site.register(VizResource)
admin.site.register(VizType)
