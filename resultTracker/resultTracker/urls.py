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
from model_tracker.views import home_view, model_view, model_list_view
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("models/", model_list_view),
    path("model_view/<int:model_id>/", model_view)


    # hold till future
    # re_path(r'^api/models/$', views.models_list),
    # ERROR re_path(r'^api/models/(?P[0-9]+)$', views.model_detail)
    # re_path(r'^api/models/([0-9]+)$', views.model_detail)

]
