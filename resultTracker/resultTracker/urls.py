"""resultTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from model_tracker.views import (
    home_view, model_view, model_form,
    model_create_API, model_list_view_API, model_detail_view_API,
    model_delete_view_API
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    # path("createModel", model_form),
    path("createModel", model_create_API),
    path('api/model/<int:model_id>/delete', model_delete_view_API),
    path("models", model_list_view_API),
    path("model_detail/<int:model_id>", model_detail_view_API),
    path("model_view/<int:model_id>", model_view)
]
