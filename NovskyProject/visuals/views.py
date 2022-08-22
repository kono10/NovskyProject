from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tag, Visual


class IndexView(generic.ListView):
    template_name = "visuals/index.html"
    context_object_name = "latest_visual_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Visual.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Visual
    context_object_name = "visual"
    template_name = "visuals/detail.html"
