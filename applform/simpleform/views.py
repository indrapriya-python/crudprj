
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import *

# Create your views here.


def pro(request):
    return render(request, "profile.html")


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        obj = UserProfile.objects.create(
            name=name, email=email, phone=phone, address=address)
        obj.save()
        return HttpResponseRedirect('/retrieve/')


def retrieve(request):
    details = UserProfile.objects.all()
    return render(request, 'table.html', {'details': details})


def delete(request,pk):
    UserProfile.objects.filter(id=pk).delete()
    return HttpResponseRedirect('/retrieve/')

def update(request, id):
    user = UserProfile.objects.get(id=id)
    return render(request, "update.html", {"user": user})

def update_data(request,):
    if request.method == "POST":
        id = request.POST['id']

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        UserProfile.objects.filter(id=id).update(name=name, email=email, phone=phone,address=address)
        return redirect("/retrieve/")

 
    
