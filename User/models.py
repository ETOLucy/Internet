from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=10000000.00)

class Bank_card(models.Model):
    card_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10000000.00)
    def bind_card(cls, user, card_name, balance = 10000000.00):
        bank_card, created = cls.objects.get_or_create(user=user, card_name=card_name, default={'balance': balance})
        return bank_card, created
