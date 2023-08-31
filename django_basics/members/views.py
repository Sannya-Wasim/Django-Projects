from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def employees(request):
    employees = Employee.objects.all().values()
    template = loader.get_template('index.html')
    context ={'employees':employees}
    return HttpResponse(template.render(context, request))

def form(request):
    return HttpResponse('T')
