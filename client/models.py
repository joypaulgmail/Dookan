from django.db import models

class detail(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    class Meta:
        db_table="detail"

class ClientDetail(models.Model):
    name=models.CharField(max_length=60)
    primary_contact=models.IntegerField()
    secondary_contact=models.IntegerField()
    address=models.TextField()
    pin=models.IntegerField()
    image=models.ImageField(upload_to="client/")
    idproof=models.ImageField(upload_to="client/id")
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    class Meta:
        db_table="clientdetail"



