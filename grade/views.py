#coding: utf-8 
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms1 import ADD_form
from os import path

# Create your views here.
def handle_uploaded_file(f):
    with open(path.join(path.dirname(path.dirname(__file__)),'GradeData','fil1','text1'),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method == 'POST':
        form1 = ADD_form(request.POST, request.FILES)
        if form1.is_valid():
            f=request.FILES['a']
            handle_uploaded_file(f)
            return HttpResponseRedirect('/success/')
    else:
        form1 = ADD_form()
    return render(request,'upload.html',{'form':form1})

def redirect1(request):
    return HttpResponse('success!')