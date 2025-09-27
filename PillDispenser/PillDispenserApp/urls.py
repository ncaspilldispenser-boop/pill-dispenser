
from django.urls import include, path

from PillDispenserApp.views import *

urlpatterns = [
    path('',LoginView.as_view(),name='login'),
    path('complaint',ComplaintView.as_view(),name='complaint'),
    path('feedback',FeedbackView.as_view(),name='feedback'),
    path('guardian',GuardianView.as_view(),name='guardian'),
    path('patient',PatientView.as_view(),name='patient'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
  
]