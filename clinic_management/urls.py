from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("", views.home, name="home"),
    path("management/patients/", views.patients, name="patients"),
    path("management/patients/new/", views.patients_new, name="patients_new"),
    path("management/patients/<uuid:id>/", views.patients_detail, name="patients_detail"),
    path("management/patients/<uuid:id>/edit", views.patients_edit, name="patients_edit"),
    path("management/patients/<uuid:id>/prepare_delete", views.patients_prepare_delete, name="patients_prepare_delete"),
    path("management/patients/<uuid:id>/delete", views.patients_delete, name="patients_delete"),
    path("management/appointments/", views.appointments, name="appointments"),
    path("management/appointments/new/", views.appointment_new, name="appointments_new"),
]
