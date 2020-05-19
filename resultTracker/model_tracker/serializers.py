# making it possible for web to consume python classes
from rest_framework import serializers
from .models import Cm_model_detail


class Cm_model_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cm_model_detail
        fields = ('base_model_name',
                  'cm_model_name',
                  'cm_model_description')
