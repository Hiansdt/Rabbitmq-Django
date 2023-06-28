from django.shortcuts import render
from .tasks import send_message
from django.http import HttpResponse

# Create your views here.

def my_pub_view(request):
    return HttpResponse("Message sent!")