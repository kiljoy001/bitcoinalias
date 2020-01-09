from django.db import models

class TransactionId(models.Model):
    #this length may need to be updated, number is from sample transaction 
    Id = models.CharField(max_length=64)
