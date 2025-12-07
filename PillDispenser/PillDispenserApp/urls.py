
from django.urls import include, path

from PillDispenserApp.views import *

urlpatterns = [

    path('',LoginView.as_view(),name='login'),
    path('complaint',ComplaintView.as_view(),name='complaint'),
    path('feedback',FeedbackView.as_view(),name='feedback'),
    path('guardian',GuardianView.as_view(),name='guardian'),
    path('patient',PatientView.as_view(),name='patient'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
    path('sendreply/<int:id>/',sendreplyview.as_view(),name='sendreply'),
    path('DeletePatient/<int:pk>/',DeletePatient.as_view()),

    # /////////////////////////// API ////////////////////////////////////////////

    path('userRegister_api',userRegister_api.as_view(),name='userRegister_api'),
    path('LoginPage_api',LoginPage_api.as_view(),name='LoginPage_api'),
    path('ViewPatientAPI',ViewPatientAPI.as_view(),name='ViewPatientAPI'),
    path('ViewMedicineAPI',ViewMedicineAPI.as_view(),name='ViewMedicineAPI'),
    path('ViewComplaintAPI/<int:id>/',ViewComplaintAPI.as_view(),name='ViewComplaintAPI'),
    path('ViewMedicalReportsAPI',ViewMedicalReportsAPI.as_view(),name='ViewMedicalReportsAPI'),
    path('ViewFeedbackAPI/<int:id>',ViewFeedbackAPI.as_view(),name='ViewFeedbackAPI'),
   
]