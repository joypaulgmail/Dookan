from django.contrib import admin
from client.models import ClientInformation
@admin.register(ClientInformation)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name","primary_contact","secondary_contact","email","address","pin","image","idproof","password")
