from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import StudentApp
from .forms import StudentAppa

# Create your views here.
def stud(request):
    data=StudentApp.objects.all()
    return render(request,"pvn11/new.html",{"data":data})

def addstu(request):
    data1=StudentApp(name=request.POST["name"],rollno=request.POST["rollno"],marks=request.POST["marks"])
    data1.save()
    return HttpResponseRedirect("/stud/")


def delstu(request,var):
    data2=StudentApp.objects.get(pk=var)
    data2.delete()
    return HttpResponseRedirect("/stud/")


def formstu(request):
    print(request.POST)
    if request.method=="POST":
        form=StudentAppa(request.POST)
        if form.is_valid():
            n=request.POST.get("name")
            n1=request.POST.get("rollno")
            n2=request.POST.get("marks")
            # print(n,n1,n2)
            StudentApp.objects.create(name=n,rollno=n1,marks=n2)
            return HttpResponseRedirect("/form/")
    else:
        form=StudentAppa()
        return render(request,"pvn11/form2.html",{"form":form})
