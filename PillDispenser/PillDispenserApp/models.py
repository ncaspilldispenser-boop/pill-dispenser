from django.db import models

# Create your models here.

class LoginModel(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    usertype = models.CharField(max_length=100, null=True, blank=True)

class PatientModel(models.Model):
    registernumber = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    LOGINID = models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True, blank=True)

class GuardianModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    LOGINID = models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True, blank=True)

class ComplaintModel(models.Model):
    date = models.DateField(max_length=100, null=True, blank=True) 
    complaint = models.CharField(max_length=100, null=True, blank=True)
    reply = models.CharField(max_length=100, null=True, blank=True)
    guardianid = models.ForeignKey(GuardianModel,on_delete=models.CASCADE,null=True, blank=True)

class FeedbackModel(models.Model):
    guardianid = models.ForeignKey(GuardianModel,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField(max_length=100, null=True, blank=True) 
    feedback = models.CharField(max_length=100, null=True, blank=True)
    rating = models.FloatField(max_length=100, null=True, blank=True) 
    

class MedicineModel(models.Model):
    medicinename = models.CharField(max_length=100, null=True, blank=True)  
    dosage = models.CharField(max_length=100, null=True, blank=True) 
    time = models.DateTimeField(max_length=100, null=True, blank=True) 
    date = models.DateField(max_length=100, null=True, blank=True) 
    discription = models.CharField(max_length=100, null=True, blank=True)
    patientid = models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True, blank=True)

class AlertModel(models.Model):    
    patientid = models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True, blank=True)
    medicineid = models.ForeignKey(MedicineModel,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField(max_length=100, null=True, blank=True) 
    Time = models.DateTimeField(max_length=100, null=True, blank=True) 

class MedicalReportsModel(models.Model):
      patientid = models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True, blank=True)
      date = models.DateField(max_length=100, null=True, blank=True)
      medicalreport = models.FileField(max_length=100, null=True, blank=True)