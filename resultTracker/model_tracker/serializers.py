# making it possible for web to consume python classes
from django.conf import settings
from rest_framework import serializers
from .models import Cm_model_detail

MAX_DESCRIPTION_LENGTH = settings.MAX_DESCRIPTION_LENGTH


class Cm_model_detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cm_model_detail
        fields = ('id', 'base_model_name',
                  'cm_model_name',
                  'cm_model_description')

    def validate_description(self, value):

        if len(value) > MAX_DESCRIPTION_LENGTH:
            raise serializers.ValidationError("Name is too long ")

        return model_description
