from django.shortcuts import render
from books.models import Book

# Create your views here.
#function based:
def home(request):

    return render(request, 'home.html')

def add(request):


    if(request.method=="POST"):
        t=request.POST['t']
        a = request.POST['a']
        p= request.POST['p']
        b=Book.objects.create(title=t,auhtor=a,price=p)
        b.save()
        return viewbook(request)
    return render(request, 'addbooks.html')

def view(request):
    k=Book.objects.all()

    return render(request, 'viewbooks.html',{'b':k})