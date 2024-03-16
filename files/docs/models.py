from django.db import models

# Create your models here.
class User(models.Model):
    document=models.FileField(null=True)
