from django.urls import path
from . import views

app_name="aspatal_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path("appointments/p/", views.AppointmentsForAPatientView.as_view(), name="patient-appointments"),
    path("appointments/d/", views.AppointmentsForADoctorView.as_view(), name="doctor-appointments"),
    path("medHistory/", views.MedicalHistoryView.as_view(), name="med-history"),
    path("prescriptions/", views.PrescriptionListView.as_view(), name="doc-prescriptions"),
    path("prescription/create", views.PrescriptionCreateView, name="doc-prescriptions-create"),
    path("appointment/create", views.AppointmentCreateView, name="appointment-create"),
    path("rdashboard/", views.rdashboard, name="r_dashboard"),
    path("hrdashboard/", views.hrdashboard, name="hr_dashboard"),
    path("hraccounting/", views.hraccounting, name="hr_accounting"),
    path("payments/", views.pateintpayments, name="pat_payments"),
]
