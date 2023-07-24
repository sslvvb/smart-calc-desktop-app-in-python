from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("graph/", views.graph, name='graph'),
    path("about/", views.about, name='about'),
    path("clean_history/", views.clean_history, name='clean_history'),
    path("background/", views.change_background, name='background'),
    path("main_color/", views.change_main_color, name='main_color'),
    path("font_size/", views.change_font_size, name='font_size'),
    path("server_ready/", views.server_ready, name='server_ready'),
]
