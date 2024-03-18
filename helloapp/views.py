from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def hellofunc(request):
    return HttpResponse('<h1>こんにちは世界のみんさん！</h1>')

class HelloClass(TemplateView):
    template_name = 'hello.html'
