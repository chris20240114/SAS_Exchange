from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seller(models.Model):
    
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255, default="")
    Contact = models.CharField(max_length=255)
    Product_type = models.CharField(max_length=255)
    Exp_choices = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    Experience = models.CharField(max_length=255, choices = Exp_choices)
    Introduction = models.CharField(max_length=255)
    Information = models.CharField(max_length=255)
    GroupChat = models.CharField(max_length=255, choices = Exp_choices)
    Questions = models.CharField(max_length=255, blank = True, null = True)
    
    def __str__(self):
        return str(self.First_Name) + " " + str(self.Last_Name)

    
#['name', 'Contact', 'Product_type', 'Experience', 'Introduction', 'Information', 'GroupChat', 'Questions']
