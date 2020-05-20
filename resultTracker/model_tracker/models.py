from django.db import models

# Create your models here.


class Cm_model_detail(models.Model):
    base_model_name = models.CharField(max_length=100, blank=True, null=True)
    cm_model_name = models.CharField(max_length=100, unique=True, )
    cm_model_description = models.CharField(
        max_length=250, blank=True)

    def __str__(self):
        return self.cm_model_name


'''
class Cm_stiffness(models.Model):
    pch_file = models.FileField(upload_to='MEDIA_ROOT/pchResult/',
     blank=True, null=True)



location_load_applied TEXT NOT NULL,
node_number REAL,
load_direction TEXT NOT NULL,
newton_mm_force REAL NOT NULL,
model_id integer NOT NULL,
FOREIGN KEY (model_id) REFER
'''
