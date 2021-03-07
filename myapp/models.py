from django.db import models
from django.utils import timezone
import datetime

class Patient(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	dob = models.DateField()
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="Inactive")
	profile_img=models.ImageField(upload_to='images/')
	other_detail=models.TextField(max_length=100)

	def __str__(self):
		return self.fname+" "+self.lname

			
class Doctor(models.Model):
	Degree=(('MBBS','MBBS'),
			 ('MD','MD'),
			  ('MS','MS'),
			   ('DM','DM'),)
	Specialization=(('Cardiology (Heart Care)','Cardiology (Heart Care)'),
				    ('Neurology','Neurology'),
					('Emergency Medicine Specialists','Emergency Medicine Specialists'),
					('Gastroenterologists','Gastroenterologists'),
					('Internal Medicine','Internal Medicine'),)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	degree=models.CharField(max_length=100,choices=Degree)
	specialization=models.CharField(max_length=100,choices=Specialization)
	dob = models.DateField()
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	consult_fees=models.IntegerField()
	profile_img=models.ImageField(upload_to='images/')
	status=models.CharField(max_length=100,default="Inactive")

	def __str__(self):
		return self.fname+" "+self.lname

class Appointment(models.Model):
	Department=(('Cardiology (Heart Care)','Cardiology (Heart Care)'),
				    ('Neurology','Neurology'),
					('Emergency Medicine Specialists','Emergency Medicine Specialists'),
					('Gastroenterologists','Gastroenterologists'),
					('Internal Medicine','Internal Medicine'),)
	Timeslot=(('9:30 to 10:00','9:30 to 10:00'),
		      ('10:30 to 11:00','10:30 to 11:00'),
		      ('11:30 to 12:00','11:30 to 12:00'),
		      ('1:30 to 2:00','1:30 to 2:00'),
		      ('2:30 to 3:00','2:30 to 3:00'),
		      ('3:30 to 4:00','3:30 to 4:00'))
	patientName=models.ForeignKey(Patient,on_delete=models.CASCADE)
	email=models.CharField(max_length=100)
	doctorName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	Department=models.CharField(max_length=100,choices=Department)
	appointmentDate=models.DateField()
	timeslot=models.CharField(max_length=100,choices=Timeslot)
	fees=models.IntegerField(default=100)
	message=models.TextField(max_length=500)
	status=models.CharField(max_length=100,default="pending")

	def __str__(self):
		return self.patientName.fname+"- "+self.doctorName.fname

class Transaction(models.Model):
	made_by = models.ForeignKey(Patient, related_name='transactions',on_delete=models.CASCADE)
	made_on = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField()
	order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
	checksum = models.CharField(max_length=100, null=True, blank=True)
	def save(self, *args, **kwargs):
		if self.order_id is None and self.made_on and self.id:
			self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
		return super().save(*args, **kwargs)

class Prescription(models.Model):
	patientName=models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctorName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	appointment_id=models.ForeignKey(Appointment,on_delete=models.CASCADE)
	Date=models.DateField()
	Description=models.TextField(max_length=500)
	status=models.CharField(max_length=100,default="pending")




	
	


# Create your models here.
