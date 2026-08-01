from django.urls import path
from . import views

#app_name = "beb"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("<int:author_id>/", views.detail, name="detail"),
    path("slide", views.slide, name="slide"),
    path("slide2", views.slide2, name="slide2"),
    path("blueslider", views.blueslider, name="blueslider"),
    path("blueslider2", views.blueslider2, name="blueslider2"),
    path("carousel", views.carousel, name="carousel"),
    path("menu", views.menu, name="menu"),
    path("camere", views.camere, name="camere"),
    path("lasala", views.lasala, name="lasala"),
    path("linkutili", views.linkutili, name="linkutili"),
    path("ilpaese", views.ilpaese, name="ilpaese"),
    path("camere_frame", views.camere_frame, name="camere_frame"),
    path("lasala_frame", views.lasala_frame, name="lasala_frame"),
    path("modal", views.modal, name="modal"),
    path("prenotazioni", views.prenotazioni, name="prenotazioni"),
    path("dovemangiare", views.dovemangiare, name="dovemangiare"),
   
   
]