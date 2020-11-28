from django.db import models
class ClientInformation(models.Model):
    name=models.CharField(max_length=60)
    primary_contact=models.CharField(max_length=15)
    secondary_contact=models.CharField(max_length=15)
    email=models.EmailField(blank=True,null=True)
    address=models.TextField()
    pin=models.CharField(max_length=15)
    image=models.ImageField(upload_to="client/")
    idproof=models.ImageField(upload_to="client/id")
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    class Meta:
        db_table="clientinformation"





