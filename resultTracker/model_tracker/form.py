from django import forms

from .models import Cm_model_detail


class model_detail(froms.ModelForm):

    class Meta:
        model = Cm_model_detail
        fields = [
            base_model_name, cm_model_name, cm_model_description]

    def clean_inputs(self):
