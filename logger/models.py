from audioop import maxpp
from django.db import models

class Connection(models.Model):
    ip = models.CharField(max_length=15)
    shell = models.CharField(max_length=256)
    user_agent = models.CharField(max_length=256)
    accept_language = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    
    
    