from django.shortcuts import render
from .tasks import send_message
from django.http import HttpResponse, JsonResponse

# Create your views here.

def send_message_view(request, username):
    send_message.delay(username)

    return JsonResponse({'message': 'Message sent!'})