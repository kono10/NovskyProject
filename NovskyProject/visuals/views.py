from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tag, Visual
from .serializers import VisualSerializer
from rest_framework import viewsets


class IndexView(generic.ListView):
    template_name = "visuals/index.html"
    context_object_name = "latest_visual_list"
    paginate_by = 10

    def get_queryset(self):
        """Return the last five published questions."""
        return Visual.objects.order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Visual
    context_object_name = "visual"
    template_name = "visuals/detail.html"


class VisualViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Visual.objects.all()
    serializer_class = VisualSerializer
    # permission_classes = [permissions.IsAuthenticated]
