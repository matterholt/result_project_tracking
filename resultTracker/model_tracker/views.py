from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse, Http404, JsonResponse

from .models import Cm_model_detail
from .serializers import Cm_model_detail_Serializer


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello track the model</h1>")


def model_view(request, model_id):
    data = {
        'id': model_id,

    }
    # convert to REST API
    status = 200
    try:
        obj = Cm_model_detail.objects.get(id=model_id)
        data["base_name"] = obj.base_model_name
        data["cm_name"] = obj.cm_model_name
        data["cm_description"] = obj.cm_model_description

    except Exception:
        data['message'] = "NOT FOUND!!"
        status = 404
    # return HttpResponse(f"<h1>Model Details for <br> {obj}</h1>")

    return JsonResponse(data, status=status)


'''
@api_view(['GET', 'POST'])
def models_list(request):
    if request.method == "GET":
        data = Cm_model_detail.objects.all()

        serializer = Cm_model_detail_Serializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = Cm_model_detail_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def model_detail(request, pk):
    # first check to see if the model is in db
    try:
        cm_model = Cm_model_detail.objects.get(pk=pk)
    except Cm_model_detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = Cm_model_detail_Serializer(
            cm_model, data=request.data, context={'request': request})

        # confirm that data matches the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        cm_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
