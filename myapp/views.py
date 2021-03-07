from django.shortcuts import render,redirect
from .models import Patient,Doctor,Appointment,Transaction,Prescription
from django.core.mail import send_mail
import random
from django.conf import settings
from datetime import date 
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request,'index.html')
def signup_patient(request):
	if request.method=='POST':
		try:
			patient=Patient.objects.get(email=request.POST['email'])
			if patient:
				msg="Email is allready Registerd"
				return render(request,'signup_patient.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				Patient.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					dob=request.POST['birthday'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					profile_img=request.FILES['profile_img'],
					other_detail=request.POST['other_details'],)
				rec=[request.POST['email'],]
				subject="OTP for Registration"
				otp=random.randint(1000,9999)
				massage="your OTP for Registration is "+str(otp)
				email_from=settings.EMAIL_HOST_USER
				send_mail(subject,massage,email_from,rec)
				return render(request,'otp.html',{'otp':otp,'email':request.POST['email']})
			else:
				msg=" Password and Confirm Password does not Matched"
				return render(request,'signup_patient.html',{'msg':msg})
	return render(request,'signup_patient.html')
def signup_doctor(request):
	if request.method=='POST':
		try:
			doctor=Doctor.objects.get(email=request.POST['email'])
			if doctor:
				msg="Email is allready Registerd"
				return render(request,'signup_doctor.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				Doctor.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					degree=request.POST['degree'],
					specialization=request.POST['specialization'],
					dob=request.POST['birthday'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					consult_fees=request.POST['consult_fees'],
					profile_img=request.FILES['profile_img'],
					)
				rec=[request.POST['email'],]
				subject="OTP for Registration"
				otp=random.randint(1000,9999)
				massage="your OTP for Registration is "+str(otp)
				email_from=settings.EMAIL_HOST_USER
				send_mail(subject,massage,email_from,rec)
				return render(request,'otp.html',{'otp':otp,'email':request.POST['email']})
			else:
				msg=" Password and Confirm Password does not Matched"
				return render(request,'signup_doctor.html',{'msg':msg})
	else:
		return render(request,'signup_doctor.html')

def login_doctor(request):
	if request.method=='POST':
		try:
			doctor=Doctor.objects.get(email=request.POST['email'],password=request.POST['password'],)
			if doctor:
				request.session['email']=doctor.email
				request.session['fname']=doctor.fname
				request.session['lname']=doctor.lname
				return render(request,'doctor.html')
		except:
			msg="Email and Password is Incorrect"
			return render(request,'login_doctor.html',{'msg':msg})
	else:
		return render(request,'login_doctor.html')
def login_patient(request):
	if request.method=='POST':
		try:
			patient=Patient.objects.get(email=request.POST['email'],password=request.POST['password'],)
			if patient:
				request.session['email']=patient.email
				request.session['fname']=patient.fname
				request.session['lname']=patient.lname
				doctor=Doctor.objects.all()
				return render(request,'book_appointment.html',{'doctor':doctor})
		except:
			msg="Email and Password is Incorrect"
			return render(request,'login_patient.html',{'msg':msg})
	else:
		return render(request,'login_patient.html')
def validate_otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	email=request.POST['email']
	myvar=""
	try:
		myvar=request.POST['myvar']
	except:
		pass
	if uotp==otp and myvar=="forgot_password":
		return render(request,'new_password.html',{'email':email})
	elif uotp==otp :
		try:
			patient=Patient.objects.get(email=email)
			if patient:
				patient.status="active"
				patient.save()
				msg="user validated Successfully"
				return render(request,'login_patient.html',{'msg':msg})
		except:
			doctor=Doctor.objects.get(email=request.POST['email'])
			if doctor:
				doctor.status="active"
				doctor.save()
				msg="user validated Successfully"
				return render(request,'login_doctor.html',{'msg':msg})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'msg':msg,'otp':otp,'email':email})
def forgot_password(request):
	if request.method=='POST':
		try:
			patient.objects.get(email=request.POST['email'])
			if patient:
				rec=[request.POST['email'],]
				subject="OTP for Registration"
				otp=random.randint(1000,9999)
				massage="your OTP for Registration is "+str(otp)
				email_from=settings.EMAIL_HOST_USER				
				send_mail(subject,massage,email_from,rec)
				myvar="forgot_password"
				return render(request,'otp.html',{'otp':otp,'email':request.POST['email'],'myvar':myvar})
			else:
				msg="Email Does Not exist"
				return render(request,'forgot_password.html',{'msg':msg})
		except:
			doctor.objects.get(email=request.POST['email'])
			if doctor:
				rec=[request.POST['email'],]
				subject="OTP for Registration"
				otp=random.randint(1000,9999)
				massage="your OTP for Registration is "+str(otp)
				email_from=settings.EMAIL_HOST_USER				
				send_mail(subject,massage,email_from,rec)
				myvar="forgot_password"
				return render(request,'otp.html',{'otp':otp,'email':request.POST['email'],'myvar':myvar})
			else:
				msg="Email Does Not exist"
				return render(request,'forgot_password.html',{'msg':msg})
	
	else:
		return render(request,'forgot_password.html')
def new_password(request):
	try:
		patient=Patient.objects.get(email=request.POST['email'])
		if patient and request.POST['new_password']==request.POST['cnew_password']:
			patient.password=request.POST['new_password']
			patient.cpassword=request.POST['new_password']
			patient.save()
			return redirect('login_patient.html')
		else:
			msg="New Password & Confirm Password Does not Matched"
			return render(request,'new_password.html',{'email':email,'msg':msg})
	except:
		doctor=Doctor.objects.get(email=request.POST['email'])
		if doctor and request.POST['new_password']==request.POST['cnew_password']:
			doctor.password=request.POST['new_password']
			doctor.cpassword=request.POST['new_password']
			doctor.save()
			return redirect('login_doctor.html')
		else:
			msg="New Password & Confirm Password Does not Matched"
			return render(request,'new_password.html',{'email':email,'msg':msg})
def patient(request):
	return render(request,'patient.html')
def doctor(request):
	return render(request,'doctor.html')
def book_appointment(request):
	if request.method=='POST':
		patient=Patient.objects.get(email=request.session['email'])
		doctor=Doctor.objects.get(fname=request.POST['dname'])
		msg="Book your appointment Successfully"
		appointments=Appointment.objects.filter(email=request.session['email'])
		return render(request,'view_appointment.html',{'msg':msg,'appointments':appointments})
	else:
		doctor=Doctor.objects.all()
		return render(request,'book_appointment.html',{'doctor':doctor})
def logout_patient(request):
	try:
		del request.session['fname']
		del request.session['lname']
		del request.session['email']
		return render(request,'index.html')
	except:
		return render(request,'index.html')
def logout_doctor(request):
	try:
		del request.session['fname']
		del request.session['lname']
		del request.session['email']
		return render(request,'index.html')
	except:
		return render(request,'index.html')
def view_appointment(request):
	flag=False
	try:
		patient=Patient.objects.get(email=request.session['email'])
		if patient:
			flag=True
			appointments=Appointment.objects.filter(patientName=patient).order_by('-id')
			return render(request,'view_appointment.html',{'appointments':appointments,'flag':flag})
	except:
		doctor=Doctor.objects.get(email=request.session['email'])
		appointments=Appointment.objects.filter(doctorName=doctor).order_by('-id')
		return render(request,'view_appointment.html',{'appointments':appointments,'flag':flag})

def view_detail(request,pk):
	flag=False 
	try:
		patient=Patient.objects.get(email=request.session['email'])
		if patient:
			appointments=Appointment.objects.get(pk=pk)
			return render(request,'view_detail.html',{'appointments':appointments,'flag':flag})
	except:
		flag=True
		appointments=Appointment.objects.get(pk=pk)
		return render(request,'view_detail.html',{'appointments':appointments,'flag':flag})
def cancel_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	appointment.delete()
	return redirect('view_appointment')

def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'pay.html')
    try:
    	patient=Patient.objects.get(email=request.session['email'])
    	amount = int(request.POST['fees'])
    except:
    	return render(request, 'book_appointment.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=patient,amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(request.session['email'])),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://localhost:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    patient=Patient.objects.get(email=request.session['email'])
    doctor=Doctor.objects.get(fname=request.POST['dname'])
    try:
    	appointment=Appointment.objects.get(doctorName=doctor,appointmentDate=request.POST['date'],timeslot=request.POST['time'],)
    	if appointment:
    		msg="This time is allready Booked"
    		return render(request,'book_appointment.html',{'msg':msg})
    except:
    	Appointment.objects.create(
				patientName=patient,
				email=request.POST['email'],
				Department=doctor.specialization,
				doctorName=doctor,
				appointmentDate=request.POST['date'],
				timeslot=request.POST['time'],
				fees=doctor.consult_fees,
				message=request.POST['message'],)
    
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return redirect('view_appointment')
        return redirect('view_appointment')

def add_prescription(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=='POST':
		doctor=Doctor.objects.get(email=request.session['email'])
		Prescription.objects.create(
			patientName=appointment.patientName,
			doctorName=appointment.doctorName,
			appointment_id=appointment,
			Date=request.POST['date'],
			Description=request.POST['Description']
			)
		appointment.status="Completed"
		appointment.save()
		return redirect('view_prescription')
	else:
		return render(request,'add_prescription.html',{'appointment':appointment})
def view_prescription(request):
	try:
		patient=Patient.objects.get(email=request.session['email'])
		if patient:
			prescription=Prescription.objects.filter(patientName=patient).order_by('-id')
			return render(request,'view_prescription.html',{'prescription':prescription})
	except:
		doctor=Doctor.objects.get(email=request.session['email'])
		if doctor:
			prescription=Prescription.objects.filter(doctorName=doctor).order_by('-id')
			return render(request,'view_prescription.html',{'prescription':prescription})

def prescription_detail(request,pk):
	prescription=Prescription.objects.get(pk=pk)
	return render(request,'prescription_detail.html',{'prescription':prescription})
	
			

	
