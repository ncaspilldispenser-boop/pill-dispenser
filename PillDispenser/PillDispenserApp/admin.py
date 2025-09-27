from django.contrib import admin

from PillDispenserApp.models import AlertModel, ComplaintModel, FeedbackModel, GuardianModel, LoginModel, MedicalReportsModel, MedicineModel, PatientModel

# Register your models here.
admin.site.register(LoginModel)
admin.site.register(PatientModel)
admin.site.register(GuardianModel)
admin.site.register(ComplaintModel)
admin.site.register(FeedbackModel)
admin.site.register(MedicineModel)
admin.site.register(AlertModel)
admin.site.register(MedicalReportsModel)