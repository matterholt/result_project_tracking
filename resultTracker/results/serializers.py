# making it possible for web to consume python classes
from rest_framework import serializers
from models import Detail_cm_model


class Detail_cm_model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_cm_model
        fields = ('base_model_name', 'cm_model_name',
                  'date_added', 'cm_model_description')


'''
    base_model_name = models.CharField(max_length=100)
    cm_model_name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    cm_model_description = models.CharField(max_length=100)
'''
