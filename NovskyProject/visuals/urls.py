from django.urls import path, include
from . import views

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"visuals", views.VisualViewSet)

app_name = "visuals"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('markdownx/', include('markdownx.urls')),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("api/", include(router.urls), name="api"),
]
