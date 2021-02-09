from django.contrib import admin
from reglog.models import product,userdetails,delivard,ReviewProduct


@admin.register(userdetails)
class registerAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","mobile","pin","password")


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ("id","name","price","image","description","makername","booking","type","time","discount","rating","clientInfo")


@admin.register(ReviewProduct)
class productAdmin(admin.ModelAdmin):
    list_display = ('product_id','username','date','review','star')




@admin.register(delivard)
class delivardAdmin(admin.ModelAdmin):
    list_display = ("name",)

