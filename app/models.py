from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class tally_ledger(models.Model):
    
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True,blank=True)
    under = models.CharField(max_length=255)
   
    mname = models.CharField(max_length=255,null=0)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=6,null=True)
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_uin = models.CharField(max_length=100,null=True)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True)

    opening_blnc_type = models.CharField(max_length=100,blank=True,null=True)

    set_odl = models.CharField(max_length=255,null=True)
    ac_holder_nm = models.CharField(max_length=255,null=True)
    acc_no = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    SA_cheque_bk = models.CharField(max_length=20,null=True)
    Echeque_p = models.CharField(max_length=20,null=True)
    SA_chequeP_con = models.CharField(max_length=20,null=True)
    
    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    valuation_type = models.CharField(max_length=100,null=True)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True)
    setalter_gstdetails = models.CharField(max_length=20,null=True)
    type_of_supply = models.CharField(max_length=100,null=True)
    assessable_value = models.CharField(max_length=100,null=True)
    appropriate_to = models.CharField(max_length=100,null=True)
    method_of_calculation = models.CharField(max_length=100,null=True)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)






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
    Particulars = models.ForeignKey(tally_ledger,on_delete=models.CASCADE)
    Date = models.DateField()

    Voucher2 = models.CharField(max_length=255)
    
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





