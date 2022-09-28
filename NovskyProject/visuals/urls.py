from django.urls import path, include, re_path
from . import views
from rest_framework import routers


# for rest api
router = routers.DefaultRouter()
router.register(r"visuals", views.VisualViewSet)

app_name = "visuals"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("api/", include(router.urls), name="api"),
    path("markdownx/", include("markdownx.urls")),
]
