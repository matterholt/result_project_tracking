from django.db import models

# Create your models here.


class Cm_model_detail(models.Model):
    base_model_name = models.CharField(max_length=100, default='none')
    cm_model_name = models.CharField(max_length=100, default='none')
    cm_model_description = models.CharField(
        max_length=250, default="i do what i want")

    def __str__(self):
        return self.cm_model_name
