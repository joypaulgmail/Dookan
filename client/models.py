from django.db import models
class ClientInformation(models.Model):
    name=models.CharField(max_length=60)
    primary_contact=models.CharField(max_length=15)
    secondary_contact=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()
    pin=models.CharField(max_length=15)
    idproof=models.ImageField(upload_to="client/id")
    password=models.CharField(max_length=50)
    unique_id=models.CharField(max_length=100,primary_key=True)

    class Meta:
        db_table="clientinformation"





