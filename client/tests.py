from django.test import TestCase


import json
import requests
def demo(id):
    BASE_URL = 'http://127.0.0.1:8000/'
    ENDPOINT = 'client/apidata/'

    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)

    for i in resp.json():
        print(i)

    dica=  {
        "name": "sneha",
        "primary_contact": "1235",
        "secondary_contact": "45688",
        "email": "sop@gmail.com",
        "address": "kpkkk",
        "pin": "12345",
        "password": "12345",
        "unique_id": "sneha"
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=dica)
#demo('25')


def clientapi(a):
    BASE_URL="http://127.0.0.1:8000/"
    ENDPOINT="client/clientapi/"
    dica = {
        "name": "Arjun",
        "primary_contact": "55555",
        "secondary_contact": "6000",
        "email": "arun@gmail.com",
        "address": "kpkkk",
        "pin": "12345",
        "password": "12345",
        "unique_id": "arunas"
    }
    resp=requests.put(BASE_URL+ENDPOINT+a,data=dica)
    if resp:
        print("ok")
#clientapi('25')

def purejson():
    BASE_URL="http://127.0.0.1:8000/"
    ENDPOINT="client/purejson"
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.json())
    print(resp.status_code)
#purejson()


def Purejson(unique_id):
    BASE_URL = "http://127.0.0.1:8000/"
    ENDPOINT = "client/clientapidata/"
    resp=requests.get(BASE_URL+ENDPOINT+unique_id)
    dic={
    "unique_id": "gopal",
    "name": "sneha",
    "primary_contact": "1235",
    "secondary_contact": "45688",
    "email": "sop@gmail.com",
    "address": "kpkkk",
    "pin": "12345",
    "password": "12345"
}
    print(resp.json())
    resp1=requests.post(BASE_URL+ENDPOINT+unique_id,data=dic)
    print(resp.status_code)

#Purejson('25')

def singleurl(unique_id=None):
    BASE_URL = "http://127.0.0.1:8000/"
    ENDPOINT = "client/singleurl/"

    data={}
    if unique_id is not None:
        data={"unique_id":unique_id}
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(type(resp))
    print(resp.json())
    print(type(resp.json()))
#singleurl('13')

def createResource():
    BASE_URL = "http://127.0.0.1:8000/"
    ENDPOINT = "client/singleurl/"
    data=  {
        "unique_id": "karampal",
        "name": "soma",
        "primary_contact": "1235",
        "secondary_contact": "45688",
        "email": "sop@gmail.com",
        "address": "kpkkk",
        "pin": "12345",
        "password": "12345"
    }

    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#createResource()

def sing(unique_id=None):
    BASE_URL = "http://127.0.0.1:8000/"
    ENDPOINT = "client/one/"


sing(420)