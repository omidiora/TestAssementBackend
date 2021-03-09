from django.db import models

# Create your models here.

interest=[
    ('school', 'school'),
    ('football', 'football'),
    ('music', 'music'),
]

budgets=[
    ('1000', '1000'),
    ('2000', '2000'),
    ('3000', '3000'),

]

class personalInfo(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    interested =models.CharField(max_length=100, choices=interest)
    budget=models.CharField(max_length=100, choices=budgets)
    images= models.ImageField(upload_to='images')
    about=models.TextField()

    def __str__(self):
        return self.firstname + self.lastname

    