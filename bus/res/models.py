from queue import Empty
from django.db import models

class uni(models.Model) :
   
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=20,default='bangalore')
    Affliation = models.TextField(default=Empty)

    def __str__(self):
        return self.name + ''