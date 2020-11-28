from django.shortcuts import render

def signup(request):
    return render(request,'client/signup.html')

def signin(request):
    return render(request,'client/signin.html')

def loggingoff(request):
    return render(request,'client/loggingoff.html')
