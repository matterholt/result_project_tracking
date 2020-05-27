from django.forms import ModelForm

from .models import Cm_model_detail


class Cm_model_form (ModelForm):

    MAX_NAME_LENGTH = 10

    class Meta:
        model = Cm_model_detail
        fields = ['cm_model_name', 'base_model_name', 'cm_model_description']

    def clean_inputs(self):
        # form validation to help
        model_name = self.clean_data.get("cm_model_name")
        if len(model_name) > MAX_NAME_LENGTH:
            raise forms.ValidationError("Name is too long ")
        return model_name
