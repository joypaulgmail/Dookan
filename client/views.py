from django.shortcuts import render,redirect
from reglog.models import product
from client.models import ClientInformation
from django.http import HttpResponse
from django.contrib import messages
from client.forms import productforms
import  random
import string


def signup(request):
    return render(request,'client/signup.html')

def client_signup_success(request):
    if request.method=="POST":
        name=request.POST.get("name")
        primary_contact=request.POST.get("primary_contact")
        secondary_contact=request.POST.get("secondary_contact")
        email=request.POST.get("email")
        address=request.POST.get("address")
        pin=request.POST.get("pin")
        id_proof=request.FILES.get("id_proof")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password==confirm_password:
            x=string.ascii_uppercase + string.digits+string.ascii_lowercase
            result_str=''.join(random.choice(x) for _ in range(6))

            unique_id=result_str

            ob=ClientInformation(name=name,primary_contact=primary_contact,secondary_contact=secondary_contact,email=email,address=address,pin=pin,idproof=id_proof,password=password,unique_id=unique_id)
            ob.save()
            return HttpResponse("sign up done")
        print("not")
        return render(request,'client/signup.html')



from client.forms import LoginForm
def signin(request):
    if request.COOKIES.get("email") and request.COOKIES.get("password"):
        return redirect("home")
    fm=LoginForm()
    '''
     if request.COOKIES.get("email") and request.COOKIES.get("password"):
        email = request.COOKIES["email"]
        password = request.COOKIES["password"]
        ob = ClientInformation.objects.raw("select * from clientinformation where email=%s and password=%s",
                                           (email, password))
        if ob:
            return render(request,'client/signin.html',{"form":fm,"email":email,"password":password})
    '''

    if request.method=="POST":
        fm=LoginForm(request.POST)
        email = request.POST.get("email")
        password=request.POST.get("password")
        ob = ClientInformation.objects.raw("select * from clientinformation where email=%s and password=%s", (email,password))
        if ob:
            for i in ob:
                request.session['email'] =i.email
                request.session['password']=i.password
                messages.success(request, i.name)
                response=redirect("home")
                response.set_cookie('email',request.session['email'])
                response.set_cookie('password',request.session['password'])

                return response
                    #redirect('home')
        else:
            messages.error(request,"Your username and password didn't match.")
            return render(request, 'client/signin.html', {"form": fm})
    return render(request,'client/signin.html',{"form":fm})


def additem(request):
    email=request.COOKIES.get('email')

    frm=productforms()
    if request.method=="POST":


        frm=productforms(request.POST,request.FILES)


        if frm.is_valid():





            frm=frm.save(commit=False)
            frm.makername=email
            frm.save()
            return HttpResponse("done")


    return render(request,'client/additem.html',{'form':frm})











def loggingoff(request):

    response=redirect('home')
    response.delete_cookie('email')
    response.delete_cookie('password')
    return response





#API START
'''from client.serializers import ClientSerializer,ClientSerialize
from rest_framework.views import APIView
from rest_framework.response import  Response

from rest_framework.renderers import JSONRenderer
class PureJson(APIView):
    def get(self,request):
        ob=ClientInformation.objects.all()
        serializer=ClientSerialize(ob,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return Response(json_data)




class ClientApi(APIView):
    def get(self,request,unique_id):
        ob=ClientInformation.objects.get(unique_id=unique_id)
        serializer=ClientSerialize(ob)
        return Response(serializer.data)

    def post(self,request,unique_id):
        serialize=ClientSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return HttpResponse(serialize.errors)

    def put(self,request,unique_id):
        ob=ClientInformation.objects.get(unique_id=unique_id)
        serializer=ClientSerialize(ob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(serializer.errors)

    def delete(self,request,unique_id):
        ob = ClientInformation.objects.get(unique_id=unique_id)
        ob.delete()
        return HttpResponse("delete")


class allorsingle(APIView):
    def get(self,request,id=None,*args,**kwargs):
        serializer=None
        if id:
            ob=ClientInformation.objects.get(unique_id=id)
            serializer=ClientSerialize(ob)
        else:
            ob=ClientInformation.objects.all()
            serializer=ClientSerialize(ob,many=True)
        return Response(serializer.data)


import json







class ShowData(APIView):
    def get(self,request,*args,**kwargs):
        ob=ClientInformation.objects.all()
        serializers=ClientSerializer(ob,many=True)
        return Response(serializers.data)


from rest_framework.renderers import JSONRenderer
class OneData(APIView):
    def get(self,request,unique_id,*args,**kwargs):
        ob=ClientInformation(name=unique_id,unique_id="45to75")
        ob.save()
        serializer=ClientSerializer(ob)
        return Response(serializer.data)

    def post(self,request,unique_id,*args,**kwargs):
        serializer=ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("ok")
        return HttpResponse(serializer.errors)



class ApiData(APIView):
    def get(self,request,*args,**kwargs):
        ob=ClientInformation.objects.all()
        serializer=ClientSerializer(ob,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("ok")
        return HttpResponse(serializer.errors)'''

#APIVIEW WITH JSON

'''import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
class SingleUrl(APIView):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        print(type(json_data))
        stream=io.BytesIO(json_data)
        print(type(stream))
        pdata=JSONParser().parse(stream)
        unique_id=pdata.get('unique_id',None)
        if unique_id is not None:
            ob=ClientInformation.objects.get(unique_id=unique_id)
            serializer=ClientSerialize(ob)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        else:
            ob=ClientInformation.objects.all()
            serializer=ClientSerialize(ob,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/jason")

    def post(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=ClientSerialize(data=pdata)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render({"text":"msz"})
            return HttpResponse(json_data,content_type="application/json")
'''




'''

from rest_framework.views import APIView
from rest_framework.response import Response
from client.serializers import ClientSerialize
class ClientApiData(APIView):
    def get(self,request,unique_id=None):
        if unique_id:
            try:
                ob = ClientInformation.objects.get(unique_id=unique_id)
            except ClientInformation.DoesNotExist:
                return Response({"msg": "You Have enter the object does not exist"})
            serializer = ClientSerialize(ob)
            return Response(serializer.data)

        else:
            ob=ClientInformation.objects.all()
            serializer=ClientSerialize(ob,many=True)
            return  Response(serializer.data)

    def post(self,request,unique_id):

        serializer=ClientSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self,request,unique_id):
        try:
            ob=ClientInformation.objects.get(unique_id=unique_id)
        except ClientInformation.DoesNotExist:
            return Response({"msz":"given object does not exist"})

        serializer=ClientSerialize(ob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return HttpResponse("put not work")

    def delete(self,request,unique_id):
        try:
            ob=ClientInformation.objects.get(unique_id=unique_id)
        except ClientInformation.DoesNotExist:
            return Response({"msz":"object does not exist"})
        ob.delete()
        return Response({"msz":"object deleted successfully"})

from rest_framework.generics import  ListAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
class ListApi(ListAPIView):
    serializer_class = ClientSerialize
    def get_queryset(self):
        qs=ClientInformation.objects.raw('select * from clientinformation')
        name=self.request.GET.get("xxx")
        if name:
            qs=ClientInformation.objects.raw('select * from clientinformation where name LIKE %s',(name,))
        return qs


class CreateApiAll(ListCreateAPIView):
    serializer_class = ClientSerialize
    def get_queryset(self):
        ob=ClientInformation.objects.raw('select * from clientinformation')
        name=self.request.GET.get("name")

        if name:
            ob = ClientInformation.objects.raw('select * from clientinformation where name=%s', (name,))
        return ob



class RetrieveApiView(RetrieveAPIView):
    queryset=ClientInformation.objects.all()
    serializer_class = ClientSerialize
    lookup_field = "unique_id"

class UpdateApiView(UpdateAPIView):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientSerialize
    lookup_field = "unique_id"

class DestroyApiView(DestroyAPIView):
    serializer_class = ClientSerialize
    queryset = ClientInformation.objects.all()
    lookup_field = "unique_id"



#MODEL MIXINS
from rest_framework import mixins
class ClientListModelMixin(mixins.ListModelMixin,CreateAPIView):
    serializer_class = ClientSerialize
    queryset = ClientInformation.objects.raw('select * from clientinformation')
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class ClientRetrieveUpdateDestroyMixins(RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientSerialize
    lookup_field = "unique_id"
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class ClientDestroyMixins(mixins.DestroyModelMixin,UpdateApiView):
    serializer_class = ClientSerialize
    queryset = ClientInformation.objects.all()
    lookup_field = "unique_id"
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Joy(APIView):
    def get(self,request,*args,**kwargs):
        name=request.GET.get("name")
        if name:
            ob=ClientInformation.objects.raw("select * from clientinformation where unique_id=%s",(str(name),))[0]
            serializer=ClientSerialize(ob)
            return Response(serializer.data)
        ob=ClientInformation.objects.raw('select * from clientinformation')
        serialize=ClientSerialize(ob,many=True)

        return Response(serialize.data)

'''














