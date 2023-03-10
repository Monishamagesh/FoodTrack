from django.shortcuts import render,redirect
from .models import Food,Food_consume
from django.contrib.auth.models import User,auth
from django.contrib import messages

def loadLogin(request):
    return render(request,"login.html")
def loadFood(request):
    return render(request,'food.html')
def addFood(request):
    if request.method=="POST":
        vname = request.POST.get('fname')
        vfname = request.POST.get('car')
        vlname = request.POST.get('fat')
        vuname = request.POST.get('pro')
        vemail = request.POST.get('cal')
        obj=Food()
        obj.name=vname
        obj.carbs=vfname
        obj.fats=vlname
        obj.protein=vuname
        obj.calories=vemail
        obj.save()
        return redirect('/index')
def Index(request):
    if request.method=='POST':
        vfood_consumed=request.POST.get('food_consume')
        consume=Food.objects.get(name=vfood_consumed)
        vuser=request.user# to get the current user
        food_consume=Food_consume(user=vuser,food_consume=consume)
        food_consume.save()
        food_item = Food.objects.all()
    else:
        food_item=Food.objects.all()
    food_selected=Food_consume.objects.filter(user=request.user)
    return render(request,'Index.html',{'food':food_item,'food_item':food_selected})

def delFood(request,fid):
    consume_food=Food_consume.objects.get(id=fid)
    consume_food.delete()
    return redirect('/index')

def userlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpass=request.POST.get('pass')
        newuser=auth.authenticate(username=vuname,password=vpass)
        if newuser is not None:
            auth.login(request,newuser)
            messages.success(request, 'Successfully Logged In')
            return redirect('/index')
        else:
            messages.success(request, 'Kindly provide correct username and password')
            return redirect('/')
