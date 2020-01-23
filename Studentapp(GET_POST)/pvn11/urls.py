from django.contrib import admin
from django.urls import path
from pvn11.views import stud,addstu,delstu,formstu

urlpatterns = [ path("stud/",stud),
                path("add/",addstu),
                path("delete/<int:var>/",delstu),
                path("form/",formstu),
                

]
