from django.forms import ModelForm

from .models import Cm_model_detail


class Cm_model_form (ModelForm):

    MAX_NAME_LENGTH = 10

    class Meta:
        model = Cm_model_detail
        fields = ['cm_model_name', 'base_model_name', 'cm_model_description']

    def clean_inputs(self):
        # form validation to help
        model_description = self.clean_data.get("cm_model_description")
        if len(model_description) > self.MAX_NAME_LENGTH:
            raise forms.ValidationError("Name is too long ")
        return model_description
