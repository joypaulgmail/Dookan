from django.shortcuts import render
from client.models import ClientInformation
from django.http import HttpResponse

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
            ob=ClientInformation(name=name,primary_contact=primary_contact,secondary_contact=secondary_contact,email=email,address=address,pin=pin,idproof=id_proof,password=password)
            ob.save()
            return HttpResponse("sign up done")
        print("not")
        return render(request,'client/signup.html')



def signin(request):
    return render(request,'client/signin.html')

def loggingoff(request):
    return render(request,'client/loggingoff.html')


