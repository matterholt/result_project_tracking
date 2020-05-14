# Admin.py
from django.contrib import admin
#django_enf
# Register your models here.
from .models import Detail_cm_model,Stiffness_result, Model_files,Project

admin.site.register(Detail_cm_model)
admin.site.register(Stiffness_result)
admin.site.register(Model_files)
admin.site.register(Project)


# models.py
# Need to confirm is correct, could test on office machine
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    project_code = models.CharField(max_length=150)
    project_part = models.CharField(max_length=150)
    def __str__(self):
        return self.project_code
    
class Model_files(models.Model):
    cm_result_pnch_file : models.FileField(max_length=1000)
    
class Stiffness_result(models.Model):
    location_load_applied = models.CharField(max_length=100)
    displacement_xyz = models.CharField(max_length=100)
    node_number = models.IntegerField()
    load_direction = models.CharField(max_length=100)
    newton_mm_force = models.IntegerField()


class Detail_cm_model(models.Model):
    base_model_name = models.CharField(max_length=100)
    cm_model_name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    cm_model_description = models.CharField(max_length=100)
    project_code = models.ForeignKey(Project, on_delete=models.CASCADE)
    model_files = models.ForeignKey()
    stiffness_results = models.ForeignKey()


    def __str__(self):
        return self.cm_model_name

