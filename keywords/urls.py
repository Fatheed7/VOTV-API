from django.urls import path
from . import views

urlpatterns = [
    path("keywords/", views.KeywordList.as_view()),
    path("keywords/<int:id>/", views.KeywordDetail.as_view()),
]