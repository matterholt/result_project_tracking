from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Detail_cm_model
from .serializers import Detail_cm_model_Serializer


@api_view(['GET', 'POST'])
def result_list(request):
    if request.method == 'GET':
        data = Detail_cm_model.objects.all()
        serializer = Detail_cm_model_Serializer(
            data, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Detail_cm_model_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
