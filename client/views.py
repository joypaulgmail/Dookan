from django.shortcuts import render,redirect
from client.models import ClientInformation
from django.http import HttpResponse
from django.contrib import messages
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
                print(request.session['email'])
                print(request.session['password'])
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


def loggingoff(request):
    response=render(request,'client/loggingoff.html')
    response.delete_cookie('email')
    response.delete_cookie('password')
    return response


