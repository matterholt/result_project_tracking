from django.db import models

"""
class Project(models.Model):
    project_code = models.CharField(max_length=150, default='FAKE')
    project_part = models.CharField(max_length=150, default='FAKE')

    def __str__(self):
        return self.project_code
"""

# Start out simple


class Detail_cm_model(models.Model):
    base_model_name = models.CharField(max_length=100, default='none')
    cm_model_name = models.CharField(max_length=100, default="newCM")
    cm_model_description = models.CharField(
        max_length=250, default="i do what i want")

    def __str__(self):
        return self.cm_model_name


'''
more research
https://www.google.com/search?client=firefox-b-1-d&q=django+upload+files#kpvalbx=_-B_AXr3IDsHEtQao7KuoAw28
class Model_files(models.Model):
    cm_result_pnch_file: models.FileField(max_length=1000)
    model_name = models.ForeignKey(Detail_cm_model, on_delete=models.CASCADE)

'''
"""

class Stiffness_result(models.Model):
    location_load_applied = models.CharField(max_length=100, default="global")
    displacement_xyz = models.CharField(max_length=100, default=100)
    node_number = models.IntegerField(default=0)
    load_direction = models.CharField(max_length=100, default='xyz?')
    newton_mm_force = models.IntegerField(default=0)
    model_name = models.ForeignKey(Detail_cm_model, on_delete=models.CASCADE)
"""
