from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # pull data from db
    # transform data
    # send email and so on
    # return HttpResponse('Hello World')
    return render(request,'hello.html',{'group':'Amigos'})