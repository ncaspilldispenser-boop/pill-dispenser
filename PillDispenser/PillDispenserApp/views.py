from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from PillDispenserApp.models import LoginModel

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
        return render(request, 'administration/complaint.html')
    
class FeedbackView(View):
    def get(self, request):
        return render(request, 'administration/feedback.html')
    
class GuardianView(View):
    def get(self, request):
        return render(request, 'administration/guardian.html')    
    
class PatientView(View):
    def get(self, request):
        return render(request, 'administration/patient.html')   
    
class AdminHome(View):
    def get(self, request):
        return render(request, 'administration/admin home.html')       