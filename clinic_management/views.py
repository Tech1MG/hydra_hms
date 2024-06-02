from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Patient
from datetime import datetime

def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email and password:
            user = authenticate(request, email = email, password = password)
            if user is not None:
                auth_login(request, user)
                return redirect("/")

    return render(request, "management/login.html")

@login_required
def logout(request):
    auth_logout(request)
    return redirect("/login")

@login_required
def home(request):
    return render(request, "management/home.html")

@login_required
def patients(request):
    patients = Patient.objects.filter(status = True)
    for patient in patients:
        patient.age = datetime.now().year - patient.birth_year
    return render(request, "management/patients.html", {'patients' : patients})

@login_required
def appointments(request):
    return render(request, "management/appointments.html")

@login_required
def patients_new(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        birth_year = request.POST.get("birth_year", "")
        phone = request.POST.get("phone", "")
        note = request.POST.get("note", "")
        histories = request.POST.get("histories", "")
        allergies = request.POST.get("allergies", "")
        medications = request.POST.get("medications", "")

        patient = Patient.objects.create(name = name, birth_year = birth_year, phone = phone,
        note = note, histories = histories, allergies = allergies, medications = medications)

        return redirect("management/patients/")
        
    return render(request, "management/creating/patient.html")

@login_required
def appointment_new(request):
    return render(request, "management/creating/appointment.html")

@login_required
def patients_detail(request, id):
    patient = Patient.objects.get(id = id)
    patient.age = datetime.now().year - patient.birth_year
    return render(request, "management/detail/patient.html", {'patient' : patient})

@login_required
def patients_edit(request, id):
    patient = Patient.objects.get(id = id)
    if request.method == "POST":
        patient.name = request.POST.get("name", "")
        patient.birth_year = request.POST.get("birth_year", "")
        patient.phone = request.POST.get("phone", "")
        patient.note = request.POST.get("note", "")
        patient.histories = request.POST.get("medical_histories", "")
        patient.allergies = request.POST.get("drug_allergies", "")
        patient.medications = request.POST.get("current_medications", "")
        patient.save()
        return redirect("/management/patients/")
    return render(request, "management/editing/patient.html", {'patient' : patient})

@login_required
def patients_prepare_delete(request, id):
    patient = Patient.objects.get(id = id)
    return render(request, "management/deleting/patient.html", {'patient' : patient})

@login_required
def patients_delete(request, id):
    patient = Patient.objects.get(id = id)
    patient.status = False
    patient.save()
    return redirect("/management/patients/")