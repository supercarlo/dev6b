from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response

from .models import Game


def index(request):
    return render_to_response('index.html')
