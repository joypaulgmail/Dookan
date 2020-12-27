from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from reglog.models import product,userdetails,delivard
from django.contrib.auth.hashers import make_password
from reglog import signals
from reglog.forms import newform,Exform,users,productforms

def home(request):
    #signals.mysig.send(sender=None,user=["hello"])
   # signals.mysign.send(sender=delivard)
    flag=None
    if request.COOKIES.get("email") and request.COOKIES.get("password"):
        flag=True

    if request.method=="POST":
        fm=Exform(request.POST)
        if fm.is_valid:
            print("ok")
    else:
        fm=Exform()




    r=product.objects.raw("select * from product")


    return render(request,"reglog/home.html",{"name":r,"flag":flag})


def order_done(request):
    if request.method=="POST":
        id=request.POST.get("id")

    return render(request,"reglog/orderdone.html",{"id":id})

def itemadd(request):
    coun=1
    x=userdetails(itemadd=coun)
    return render(request,"reglog/home.html",{"name":r})

def register(request):
    return render(request, "reglog/register.html")







def signupsuccess(request):

    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rpassword=request.POST.get("rpassword")





        if password==rpassword:
            #password=make_password(password)
            details=userdetails(name=name,mobile=mobile,email=email,password= password)
            details.save()
            object = userdetails.objects.get(name=name)
            name = object.name
            r = product.objects.all()
            messages.success(request,"welcome"+object.name)
            return redirect('home')

            #return render(request,"reglog/home.html",{"k":name,"name":r})




        else:
            return render(request, "reglog/register.html")

from django.contrib.auth.decorators import login_required
@login_required()
def result(request):

    return render(request,"reglog/result.html")

def signin(request):
    return render(request,"reglog/signin.html")



from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

'''def signinsuccess(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login success")
            return render(request,'reglog/home.html',{'username':username})
        #user=userdetails.objects.get(email=username,password=password)


        else:
            messages.error(request,"invalid username or password")
            return render(request, "reglog/signin.html")'''


from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
def signinsuccess(request):
    fm=RegistrationForm()
    if request.method=="POST":
        fm=RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("ok")

            return HttpResponse("register done")
    return render(request, 'demo/register.html', {"fm": fm})







def signout(request):
    logout(request)
    return redirect('home')

def newfrm(request):
    if request.method == "POST":
        frm = newform(request.POST)
        if frm.is_valid():
            print(frm)



    else:
        print("not valid")
        frm=newform()


    return render(request,"reglog/forms.html",{"user":frm})





from django.contrib.auth.decorators import login_required

def additem(request):
    frm=productforms()
    if request.method=="POST":
        frm=productforms(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return HttpResponse("done")


    return render(request,'reglog/additem.html',{'form':frm})
    
'''

def additem(request):
    return render(request,'reglog/addit.html')

def submita(request):
    if request.method=="POST":
        name=request.POST.get('name')
        price= request.POST.get('price')
        image= request.FILE.get('image')
        des=request.POST.get('des')
        x=product(name=name,price=price,image=image,description=des)
        x.save()
        return HttpResponse("ok")
    return HttpResponse("not ok")

'''


