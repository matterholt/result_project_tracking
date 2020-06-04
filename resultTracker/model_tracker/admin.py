from django.contrib import admin

# Register your models here.
from .models import Cm_model_detail


class ModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'base_model_name']
    search_fields = ['user__username', 'base_model_name']

    class Meta:
        model = Cm_model_detail


admin.site.register(Cm_model_detail, ModelAdmin)


# shell
# qs = Cm_model_detail.objects.filter(base_model_name = "v00")
# qs2 = Cm_model_detail.objects.filter(user__username = "matterholt")
