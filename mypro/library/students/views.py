from django.shortcuts import render

# Create your views here.
#function based:

def rgr(request):
    return render(request,'register.html')

def log(request):
    return render(request,'login.html')
