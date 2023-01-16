from django.urls import path
from . import views

urlpatterns = [
    path("artifacts/", views.ArtifactList.as_view()),
    path("artifacts/<int:id>/", views.ArtifactDetail.as_view()),
]