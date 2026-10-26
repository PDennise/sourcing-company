from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("industries/", views.industries, name="industries"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("schedule-consultation/", views.consultation, name="consultation"),
    path("submit-rfp/", views.rfp, name="rfp"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]
