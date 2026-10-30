from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu_page, name="menu"),
    path("reserve/", views.reserve, name="reserve"),
]
