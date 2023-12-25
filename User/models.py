from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=10000000.00)

class Order(models.Model):
    product_id = models.IntegerField()
    property1 = models.CharField(max_length=255)
    property2 = models.CharField(max_length=255)
    property3 = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Bank_card(models.Model):
    card_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10000000.00)
    def bind_card(cls, user, card_name, balance = 10000000.00):
        bank_card, created = cls.objects.get_or_create(user=user, card_name=card_name, default={'balance': balance})
        return bank_card, created

class Project(models.Model):
    
    project_name = models.CharField(max_length=20)
    st_time = models.CharField(max_length=20)
    ed_time = models.CharField(max_length=20)
    chat_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

class now_project(models.Model):
    complished = models.CharField(max_length=20)
    require_days = models.CharField(max_length=20)