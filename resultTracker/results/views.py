from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# django part 3!!

# Home page


def index(request):
    return HttpResponse("Keep track of your results to excel")


# Add Results

# View Results by model name

#
