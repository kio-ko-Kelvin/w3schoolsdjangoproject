from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(auto_now_add=True, null=True)