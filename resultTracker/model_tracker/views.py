from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse, Http404, JsonResponse

from .models import Cm_model_detail
from .forms import Cm_model_form
from .serializers import Cm_model_detail_Serializer


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello track the model</h1>") #--> static
    return render(request, "pages/home.html", context={}, status=200)


def model_list_view(request, *args, **kwargs):
    """
    List of all models added to the database
    User will be able to retrieve all models added under the 
    assigned project which will be implemented in the future
    """
    qs = Cm_model_detail.objects.all()
    model_list = [{"id": x.id,
                   # REMOVE BASE MODEL FROM TABLE REDUCE AMOUNT OF INFO ON MAIN PAGE??
                   "base_model_name": x.base_model_name,
                   "cm_model_name": x.cm_model_name,
                   "cm_model_description": x.cm_model_description
                   } for x in qs]  # ! look into the way of looping!!

    data = {
        "isUser": False,
        "response": model_list
    }
    return JsonResponse(data)


def model_form(request, *args, **kwargs):
    # https://youtu.be/f1R_bykXHGE?t=6804

    form = Cm_model_form(request.POST or None)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = Cm_model_form()

    return render(request, "components/form.html", context={"form": form})


def model_detail_view(request, model_id):
    data = {
        'id': model_id,
    }
    try:
        model_detail = Cm_model_detail(id=model_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "pages/modelDetail.html", context={"id": model_id},
                  status=200)


def model_view(request, model_id):
    data = {
        'id': model_id,
    }
    # convert to REST API
    status = 200
    try:
        # searches the cm model detail to get model detail
        obj = Cm_model_detail.objects.get(id=model_id)
        data["base_model_name"] = obj.base_model_name
        data["cm_model_name"] = obj.cm_model_name
        data["cm_model_description"] = obj.cm_model_description
        # searches the results DB to retrive results or judgement of analysis??
        # CREATE A NEW DATABASE WITH JUDGEMENT, stiffness, dura, static , and other

    except Exception:
        data['message'] = "NOT FOUND!!"
        status = 404

    return JsonResponse(data, status=status)


'''
Home previous example

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
