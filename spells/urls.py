from django.urls import path
from . import views

urlpatterns = [
    path("spells/", views.SpellList.as_view()),
    path("spells/<int:id>/", views.SpellDetail.as_view()),
]