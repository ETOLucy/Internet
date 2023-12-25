from django.contrib import admin
from .models import Users, Order, Bank_card, Project, now_project
# Register your models here.
admin.site.register([Users, Order, Bank_card, Project, now_project])