from django.contrib import admin

# Register your models here.
from .models import Detail_cm_model, Stiffness_result, Model_files, Project

admin.site.register(Detail_cm_model)
admin.site.register(Stiffness_result)
admin.site.register(Model_files)
admin.site.register(Project)
