from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from PillDispenserApp.serializers import *
from PillDispenserApp.models import *


# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request,'administration/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = LoginModel.objects.get(username = username, password = password)
            request.session['user_id'] = obj.id
            if obj.usertype == 'admin':
               return HttpResponse('''<script>alert('Login successful');window.location='/AdminHome'</script>''')
            else:
                return HttpResponse('''<script>alert('Login successful');window.location='/'<script>''')
        except LoginModel.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid username or password');window.location='/'</script>''')
        
class ComplaintView(View):
    def get(self, request):
        obj = ComplaintModel.objects.all()
        return render(request, 'administration/complaint.html', {'val': obj})
    
class sendreplyview(View):
    def post(self,request,id):
        complaint = ComplaintModel.objects.get(id=id)
        reply_text = request.POST.get('reply')
        complaint.reply = reply_text
        complaint.save()
       
        return redirect('complaint')
    
class FeedbackView(View):
    def get(self, request):
        obj = FeedbackModel.objects.all()
        return render(request, 'administration/feedback.html', {'val': obj})
    
class GuardianView(View):
    def get(self, request):
        obj = GuardianModel.objects.all()
        return render(request, 'administration/guardian.html', {'val': obj})    
    
class PatientView(View):
    def get(self, request):
         obj = PatientModel.objects.all()
         return render(request, 'administration/patient.html', {'val': obj})   
    
class AdminHome(View):
    def get(self, request):
        return render(request, 'administration/admin home.html')       
    
class DeletePatient(View):
    def get(self,request,pk):
        obj = LoginModel.objects.get(pk=pk)
        obj.delete()
        return HttpResponse('''<script>alert('deleted successfully');window.location='/patient'</script>''')
    

# ///////////////////////////////////////// API //////////////////////////////////////////////////////////////

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class userRegister_api(APIView):
    def post(self, request):
        print("#########################" , request.data)

        user_serial = GuardianSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(usertype='Guardian')
            user_serial.save(LOGINID=login_profile)

            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        return Response({
            'login_error' : login_serial.errors if not login_valid else None,
            'user_error' : user_serial.errors if not data_valid else None
        },status=status.HTTP_400_BAD_REQUEST)

class LoginPage_api(APIView):
    def post(self,request):
        print("+++++++++++++",request.data)
        response_dict = {}

        #get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        
        #validate input
        if not username or not password:
            response_dict["message"]="failed"
            return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
        
        #fetch the user from LoginTable
        t_user = LoginModel.objects.filter(username=username, password=password).first()

        if not t_user:
            response_dict["message"]="Failed"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            response_dict["message"]="success"
            response_dict["login_id"]=t_user.id
            response_dict["UserType"]=t_user.usertype

            return Response(response_dict,status=status.HTTP_200_OK)


class ViewPatientAPI(APIView):
   def get(self,request):
       c=PatientModel.objects.all()
       serializer=PatientSerializer(c, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
   
class ViewMedicineAPI(APIView):
   def get(self,request):
       c=MedicineModel.objects.all()
       serializer=MedicineSerializer(c, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
   
class ViewComplaintAPI(APIView):
   def get(self,request,id):
       c=ComplaintModel.objects.filter(guardianid__id=id)
       serializer=ComplaintSerializer(c, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
   
   def post(self,request,id):
       print("+++++++++++++",request.data)
       guardian = GuardianModel.objects.get(LOGINID__id=id)
       serializer=ComplaintSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(guardianid=guardian, reply="pending")
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class ViewMedicalReportsAPI(APIView):
   def get(self,request):
       c=MedicalReportsModel.objects.all()
       serializer=MedicalReportsSerializer(c, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
   

class ViewFeedbackAPI(APIView):
     def post(self,request,id):
       guardian = GuardianModel.objects.get(LOGINID_id=id)
       serializer=FeedbackSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(guardianid=guardian)
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
