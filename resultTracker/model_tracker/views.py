from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse, Http404, JsonResponse

from .models import Cm_model_detail
from .forms import Cm_model_form
from .serializers import Cm_model_detail_Serializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello track the model</h1>") #--> static
    return render(request, "pages/home.html", context={}, status=200)

# add decorators to assign what method you would like to request


@api_view(['GET'])
def model_list_view_API(request, *arg, **kwargs):
    qs = Cm_model_detail.objects.all()

    serializer = Cm_model_detail_Serializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def model_detail_view_API(request, model_id, * arg, **kwargs):
    qs = Cm_model_detail.objects.filter(id=model_id)
    if not qs:
        return Respose({'message': "item not found"}, status=404)
    obj = qs.first()
    serializer = Cm_model_detail_Serializer(obj)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def model_create_API(request, *args, **kwargs):

    serializer = Cm_model_detail_Serializer(data=request.POST)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


def model_list_view_pureDjango(request, *args, **kwargs):
    """
    List of all models added to the database
    User will be able to retrieve all models added under the
    assigned project which will be implemented in the future
    """
    qs = Cm_model_detail.objects.all()
    model_list = [x.serialize() for x in qs]

    data = {
        "isUser": False,
        "response": model_list
    }
    return JsonResponse(data)


def model_form(request, *args, **kwargs):
    user = request.user

    if not user.is_authenticated:

        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)

    form = Cm_model_form(request.POST or None)
    next_url = request.POST.get('next') or None
    print(request.is_ajax)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()

        if request.is_ajax() is True:
            return JsonResponse(obj.serialize(), status=201)

        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)

    form = Cm_model_form()

    return render(request, "components/form.html", context={"form": form})


# def model_detail_view(request, model_id):
#     data = {
#         'id': model_id,
#     }
#     try:
#         model_detail = Cm_model_detail(id=model_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "pages/modelDetail.html", context={"id": model_id},
#                   status=200)


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
