from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class statistics_Vouchers(models.Model):
    Vouchers_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Vouchers_name

class statistics_Accounts(models.Model):
    Accounts_name =models.CharField(max_length=255)

    def __str__(self):
        return self.Accounts_name 



class Months(models.Model):
    month_name = models.CharField(max_length=255)

    def __str__(self):
        return self.month_name     


class statistics_Voucher_Register(models.Model):
    Voucher = models.ForeignKey(statistics_Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Voucher2 = models.CharField(max_length=255,null=True,blank=True)
    Date = models.DateField()

    Particulars = models.CharField(max_length=255)
    # Vch_Type = models.CharField(max_length=255)
    # Vch_No = models.IntegerField()
    Debit_Amount = models.IntegerField(default="",null=True,blank=True)
    Credit_Amount = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name

class statistics_Voucher_count(models.Model):
    Voucher = models.ForeignKey(statistics_Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Total_Voucher = models.IntegerField(default="",null=True,blank=True)
    # Cancelled = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name


class statistics_Total_Voucher(models.Model):
    Voucher = models.ForeignKey(statistics_Vouchers,on_delete=models.CASCADE)
    Total = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name


class statistics_Accounts_Total(models.Model):
    Accounts = models.ForeignKey(statistics_Accounts,on_delete=models.CASCADE)
    Total = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.Accounts.Accounts_name





