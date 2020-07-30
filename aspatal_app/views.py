from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import UserProfile

def home(request):
    return render(request,'aspatal_app/home.html')

def about(request):
    return render(request,'aspatal_app/about.html')

def contact(request):
    return render(request, 'aspatal_app/contact.html')

class AppointmentsForAPatientView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'users:login'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentsForADoctorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)


class MedicalHistoryView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)


class PrescriptionListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'users:login'

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user)


@login_required(login_url='/login/')
def PrescriptionCreateView(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()
            return redirect('aspatal_app:doc-prescriptions')
    else:
        form = PrescriptionForm()
    return render(request, 'aspatal_app/prescription_create.html', {'form': form})


@login_required(login_url='/login/')
def AppointmentCreateView(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('aspatal_app:r_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'aspatal_app/appointment_create.html', {'form': form})


@login_required(login_url='/login/')
def rdashboard(request):
    if request.method == "GET" and request.user.registeras == "R":
        context = {
            "totalApp" : len(Appointment.objects.all()),
            "compApp" : len(Appointment.objects.filter(status="Completed")),
            "pendApp" : len(Appointment.objects.filter(status="Pending")),
            "app_list" : Appointment.objects.all(),
            "pat_list" : UserProfile.objects.filter(user__registeras="P")[:5]
        }
        return render(request, 'aspatal_app/recp_dashboard.html', context=context)


@login_required(login_url='/login/')
def hrdashboard(request):
    if request.method == "GET" and request.user.registeras == "HR":
        context = {
            "totalPat" : len(User.objects.filter(registeras="P")),
            "totalDoc" : len(User.objects.filter(registeras="D")),
            "ondutyDoc" : len(UserProfile.objects.filter(status="Active").filter(user__registeras="D")),
            "doc_list" : UserProfile.objects.filter(user__registeras="D")
        }
        return render(request, 'aspatal_app/hr_dashboard.html', context=context)


@login_required(login_url='/login/')
def hraccounting(request):
    if request.method == "GET" and request.user.registeras == "HR":
        context = {
            "payment_ind" : Payment.objects.filter(payment_type="I"),
            "payment_cons" : Payment.objects.filter(payment_type="C"),
        }
        return render(request, 'aspatal_app/accounting.html', context=context)


@login_required(login_url='/login/')
def pateintpayments(request):
    if request.method == "GET":
        context = {
            "payment_me" : Payment.objects.filter(patient=request.user),
        }
        return render(request, 'aspatal_app/payment_invoice.html', context=context)
