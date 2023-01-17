from django.urls import path
from . import views

urlpatterns = [
    path("cards/", views.CardList.as_view()),
    path("cards/<int:id>/", views.CardDetail.as_view()),
]