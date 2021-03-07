from django.contrib import admin
from .models import Patient,Doctor,Appointment,Transaction,Prescription

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Transaction)
admin.site.register(Prescription)

# Register your models here.
