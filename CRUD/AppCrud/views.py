from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    return render(request,'index.html')
def insertData(request):
    show = Student.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender = request.POST['gender']
        user = Student(name=name,email=email,age=age,gender=gender)
        user.save()
        if user.save():
            messages.info(request,'Data Successfully entered')
    return render(request,'index.html',{'shows':show})
def update(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender = request.POST['gender']
        user = Student.objects.get(id=id)
        user.name=name
        user.email=email
        user.age=age
        user.gender=gender
        user.save()
        return redirect("/insert")
    data=Student.objects.get(id=id)
    return render(request,'update.html',{'datas':data})
def delete(request,id):
    user = Student.objects.get(id=id)
    user.delete()
    return redirect('/insert')