from clients.models import Address, City, Client, Province
from django.contrib import admin

# Register your models here.
from .models import Province, City, Address, Client


admin.site.register(Province)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Client)
