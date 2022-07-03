from atexit import register
from django.contrib import admin
from .models import Customer, Communication, SentEmail

admin.site.register(Customer)
admin.site.register(Communication)
admin.site.register(SentEmail)