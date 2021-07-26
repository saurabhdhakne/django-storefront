from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html',{ 'name' : 'srb', 'surname' : 'dhakne' })
