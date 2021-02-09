from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from reglog.models import product,userdetails,delivard,ReviewProduct
from client.models import ClientInformation
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




    r=product.objects.raw("select * from product limit 20")
    #length=len(r)#14
   # x=length%4
   # length=length-x
    #print(length)
    #r = product.objects.raw("select * from product limit %s",(length,))



    return render(request,"reglog/home.html",{"name":r,"flag":flag})

def item_details(request):
    return render(request,"reglog/itemdetail.html")

def product_detail(request,id):
    print(id)
    x=product.objects.get(id=id)
    email = request.COOKIES["email"]
    review=ReviewProduct.objects.filter(product_id=id)


    return render(request,"reglog/review.html",{"item":x,"email":email,"review":review})

from django.utils import timezone

from dateutil.tz import *
from datetime import datetime
from django.db import connection
def review(request):
    if request.method=="POST":
        review=request.POST.get("review")
        item_id=request.POST.get("item_id")
        star=request.POST.get("star")
        print(star)
        email = request.COOKIES["email"]
        now = datetime.now()

        #ob = ReviewProduct.objects.create(product_id=item_id, review=review, date=now, username=email, star=star)
        #ob=ReviewProduct.objects.raw("INSERT INTO reviewproduct VALUES(%s,%s,%s,%s,%s)",['75','SOP@.com','2017-07-19','LOVE','5'])
        cursor=connection.cursor()
        cursor=cursor.execute("insert into reviewproduct(product_id,username,date,review,star)values(%s,%s,%s,%s,%s)",(item_id,email,now,review,star))


        return redirect('/')











def order_done(request):
    if  request.COOKIES.get("email") and request.COOKIES.get("password"):


        if request.method=="POST":
            makername=request.POST.get("makername")
            name=request.POST.get("item")
            query=product.objects.filter(makername=makername).filter(name=name)[0]

            product_name=query.name


            booking=str(int(query.booking)+1)





            ob=product.objects.filter(makername=makername).filter(name=name).update(booking=booking)
        #ob=product.objects.raw("UPDATE product SET booking=1 WHERE makername=%s",(makername,))
            print(ob)
            print(ob)
            x=request.COOKIES["email"]
            print(x)



        return render(request,"reglog/orderdone.html",{"id":makername,"query":query,"email":x})


    else:
        return render(request,"reglog/signin.html")

def itemadd(request):
    coun=1
    x=userdetails(itemadd=coun)
    return render(request,"reglog/home.html",{"name":r})


def reg(request):
    return render(request, "reglog/register.html")


def register(request):
    return redirect('reg')









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
    flag = None
    if request.COOKIES.get("email") and request.COOKIES.get("password"):
        #email=request.COOKIES.get("email")
        #password=request.COOKIES.get("password")

        flag = True
    if request.method=="POST":
        search=request.POST.get("srch")
        city=request.POST.get('city')
        some_var = request.POST.get('che')
        print("hello",some_var)




        row = product.objects.raw("select * from product where type=%s", (search,))

        print(len(row))
        return render(request, "reglog/home.html",{"name":row,"flag":flag,'city':city})



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

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get("password")

        query=userdetails.objects.filter(email=username).filter(password=password)[0]
        if query:
            response=redirect("home")
            response.set_cookie('email',username)
            response.set_cookie('password',password)
            return response

    return render(request, 'reglog/signin.html', {"fm": fm})


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

def today(request):
    flag = None
    if request.COOKIES.get("email") and request.COOKIES.get("password"):
        flag=True
        r = product.objects.raw("select * from product where discount>1 order by discount desc")

        return render(request,'reglog/todays_deal.html',{'name':r,'flag':flag})





from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.db import connection
@receiver(pre_save,sender=product)
def hell(sender,instance,**kwargs):


    highest_booking="select max(booking) from product limit 1"
    cursor=connection.cursor()
    cursor.execute( highest_booking)
    x=cursor.fetchone()
    highest_booking=int("".join(map(str,x)))
    booking = int(instance.booking)*4
    instance.rating=highest_booking/booking















def todays_deal(request):
    return redirect('todays')





def dokan_offer(request):
    flag = None
    if request.COOKIES.get("email") and request.COOKIES.get("password"):
        flag = True
        r = product.objects.raw("select * from product")
        return render(request, 'reglog/dokan_offer.html', {'name': r, 'flag': flag})



def dkn(request):
    return redirect('dokan_offer')


from reglog.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from reglog.authentications import CustomAuthentication,CustomAuthenticationByKey
from reglog.permissions import GetOnly,GetOrPost
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class ProductViewset(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer



from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
class ListProductApi(ListAPIView):
    queryset=product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
class DempApi(APIView):

    def get(self,request):
        query=product.objects.all()
        serializer=ProductSerializer(query,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    def post(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=ProductSerializer(data=pdata)     #files=request.FILES
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)


from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class ViewsetProduct(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]




'''

class ProductViewset(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
'''


'''
from reglog.permissions import GetOnly,GetOrPost
from reglog.authentications import CustomAuthentication

class ProductViewset(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [CustomAuthentication,]
    permission_classes = [GetOrPost,]
    '''








from django.contrib.auth.decorators import login_required


    
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


