from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField (max_length=50)
    address = models.CharField (max_length=50)
    state = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    pincode = models.CharField (max_length=10)
    telphone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    fyearbgn=models.DateField()
    booksbgn=models.DateField()
    curncysymbl=models.CharField(max_length=10)
    crncyname=models.CharField(max_length=10)

class empgroup(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField (max_length=50)


class empgroup2(models.Model):
    groupname = models.CharField(max_length=50)
    groupalias = models.CharField (max_length=50)
    groupunder = models.CharField (max_length=50)
   
    