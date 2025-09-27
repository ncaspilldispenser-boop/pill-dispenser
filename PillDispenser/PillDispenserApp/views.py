from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

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
        