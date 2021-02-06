from django.db import models
from client.models import ClientInformation
class userdetails(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    password=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    pin=models.CharField(max_length=30)
    image=models.ImageField(upload_to="profilephoto")
    itemadd=models.IntegerField(blank=True,null=True)



    def __str__(self):
        return self.name
    class Meta:
        db_table = "userdetails"


class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    description=models.TextField()
    makername=models.CharField(max_length=50,blank=True,null=True)
    booking=models.CharField(max_length=50,blank=True,null=True)
    type=models.CharField(max_length=50,blank=True,null=True)
    time=models.CharField(max_length=50,blank=True,null=True)
    discount=models.IntegerField(blank=True,null=True)
    rating=models.IntegerField(blank=True,null=True)
    review=models.CharField(max_length=500,blank=True,null=True)
    clientInfo=models.ForeignKey(ClientInformation,blank=True,null=True,on_delete=models.CASCADE)



    def __str__(self):

        return self.name

    class Meta:
        db_table = "product"




class delivard(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
    class Meta:
        db_table="deliverd"






