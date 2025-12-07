from rest_framework.serializers import ModelSerializer


from PillDispenserApp.models import *



class PatientSerializer(ModelSerializer):
    class Meta:
        model = PatientModel
        fields =['registernumber', 'name', 'phone',' email',' address','gender','LOGINID']

class GuardianSerializer(ModelSerializer):
    class Meta:
        model = GuardianModel
        fields =[ 'name', 'phone','email','address','gender']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintModel
        fields = ['complaint','guardianid']

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = ['feedback','rating']

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = MedicineModel
        fields =['medicinename','dosage','time','date','discription','patientid']

class AlertSerializer(ModelSerializer):
    class Meta:
        model = AlertModel
        fields =  ['patientid','medicineid','date','time']      

class MedicalReportsSerializer(ModelSerializer):
    class Meta:
        model = MedicalReportsModel
        fields =['patientid','date','medicalreport']

class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginModel
        fields =['username','password','usertype']
