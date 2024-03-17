from django.db import models

# Create your models here.
class User(models.Model):
    document=models.FileField(null=True)


class Contact(models.Model):
    name= models.CharField(max_length=122) # here, name is an attribute and charfield is known as formfield which determines the datatype of attribute.
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

def __str__(self):
    return self.name
