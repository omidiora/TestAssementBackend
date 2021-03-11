from django.db import models

# Create your models here.



class personalInfo(models.Model):
    firstname = models.CharField(max_length=50 )
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100 ,)
    contact = models.CharField( max_length=100 ,blank=True )
    company = models.CharField(max_length=100 , blank=True)
    interested =models.CharField(max_length=100,    blank=True )
    budget=models.CharField(max_length=100, blank=True ,)
    images= models.ImageField(upload_to='images' , blank=True  ,null=True)
    about=models.TextField(blank=True)

    def __str__(self):
        return self.firstname 

    
    