from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup_patient/',views.signup_patient,name='signup_patient'),
    path('signup_doctor/',views.signup_doctor,name='signup_doctor'),
    path('login_doctor/',views.login_doctor,name='login_doctor'),
    path('login_patient/',views.login_patient,name='login_patient'),
    path('validate_otp/',views.validate_otp,name='validate_otp'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('patient/',views.patient,name='patient'),
    path('doctor/',views.doctor,name='doctor'),
    path('book_appointment/',views.book_appointment,name='book_appointment'),
    path('logout_patient/',views.logout_patient,name='logout_patient'),
    path('logout_doctor/',views.logout_doctor,name='logout_doctor'),
    path('view_appointment/',views.view_appointment,name='view_appointment'),
    path('view_detail/<int:pk>/',views.view_detail,name='view_detail'),
    path('cancel_appointment/<int:pk>/',views.cancel_appointment,name='cancel_appointment'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('add_prescription/<int:pk>/',views.add_prescription,name='add_prescription'),
    path('view_prescription/',views.view_prescription,name='view_prescription'),
    path('prescription_detail/<int:pk>/',views.prescription_detail,name='prescription_detail'),



    
]
