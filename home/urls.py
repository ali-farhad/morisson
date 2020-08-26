from django.urls import path
from . import views


app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.services, name="services"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("careers/", views.careers, name="careers"),
    path("apply/", views.apply, name="apply"),
]

