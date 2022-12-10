import datetime
from django.shortcuts import HttpResponse, redirect

# Create your views here.

def main_view(request):
    return HttpResponse("Hello! It's my first view!")

def google_redirect_view(request):
    return redirect('https://google.com')

def youtube_redirect_view(request):
    return redirect('https://youtube.com')

def view_hello(request):
    return HttpResponse("Hello! It's my project")

def view_now_date(request):
    current_date = datetime.datetime.today().date()
    return HttpResponse(f'Current date: \n{current_date}')

def view_goodby(request):
    return HttpResponse("Goodby user!")
