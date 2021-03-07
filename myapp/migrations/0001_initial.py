# Generated by Django 3.0 on 2021-02-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('degree', models.CharField(choices=[('MBBS', 'MBBS'), ('MD', 'MD'), ('MS', 'MS'), ('DM', 'DM')], max_length=100)),
                ('specialization', models.CharField(choices=[('Cardiology (Heart Care)', 'Cardiology (Heart Care)'), ('Neurology', 'Neurology'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Gastroenterologists', 'Gastroenterologists'), ('Internal Medicine', 'Internal Medicine')], max_length=100)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('consult_fees', models.IntegerField()),
                ('profile_img', models.ImageField(upload_to='images/')),
                ('status', models.CharField(default='Inactive', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('status', models.CharField(default='Inactive', max_length=100)),
                ('profile_img', models.ImageField(upload_to='images/')),
                ('other_detail', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('Department', models.CharField(choices=[('Cardiology (Heart Care)', 'Cardiology (Heart Care)'), ('Neurology', 'Neurology'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Gastroenterologists', 'Gastroenterologists'), ('Internal Medicine', 'Internal Medicine')], max_length=100)),
                ('appointmentDate', models.DateField()),
                ('timeslot', models.CharField(choices=[('9:30 to 10:00', '9:30 to 10:00'), ('10:30 to 11:00', '10:30 to 11:00'), ('11:30 to 12:00', '11:30 to 12:00'), ('1:30 to 2:00', '1:30 to 2:00'), ('2:30 to 3:00', '2:30 to 3:00'), ('3:30 to 4:00', '3:30 to 4:00')], max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('doctorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Doctor')),
                ('patientName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
    ]
