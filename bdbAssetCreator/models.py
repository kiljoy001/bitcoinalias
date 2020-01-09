from django.db import models
from django.urls import reverse 

class TransactionId(models.Model):
    #this length may need to be updated, number is from sample transaction 
    Id = models.CharField(max_length=64)

    def __str__(self):
        return self.Id

    def get_absolute_url(self):
        return reverse('')
    
