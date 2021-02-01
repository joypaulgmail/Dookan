from django.contrib import admin
from reglog.models import product,userdetails,delivard


@admin.register(userdetails)

class registerAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","mobile","pin","password")


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ("id","name","price","image","description","makername","booking","type","time","clientInfo")

@admin.register(delivard)
class delivardAdmin(admin.ModelAdmin):
    list_display = ("name",)

