from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from todolist.models import Task
# Create your views here.
# def index(request):
#     if request.user.is_anonymous:
#         return redirect("/")
#     else:
#         return render(request,'index.html')

def loginUser(request):
    if  request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
      
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/task")
        
    # A backend authenticated the credentials
    
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')    

def logoutuser(request):
    logout(request)
    return redirect("/")

def task(request):
    if request.user.is_anonymous:
        return redirect("/")
    
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        isinstance= Task(title=title,desc=desc)
        isinstance.save()
        print(title,desc)
        # context={"success":True}
    return render(request,"task.html")

def todolist(request):
    if request.user.is_anonymous:
        return redirect("/")
        
    else:
        alltasks= Task.objects.all()
        context={'tasks':alltasks}
    # if request.method=="POST":
        return render(request,"todolist.html",context)
