from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def Topic_Form(request):
    SFO=Topic_Forms()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=Topic_Forms(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'Topic_Form.html',d)


def Player_Form(request):
    SFO=Player_Forms()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=Player_Forms(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'Player_Form.html',d)