from django.db import models
from localflavor import pl
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    id = models.CharField(max_length=11,verbose_name = 'PESEL',unique=True,primary_key=True)
    password = models.CharField(max_length=200)
    balance = models.FloatField(default=0)
    account_number = models.CharField(max_length=200,default="0000 0000 0000")

