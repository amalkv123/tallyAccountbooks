from django.shortcuts import render,redirect
import os
from app.models import Months,statistics_Voucher_count,statistics_Total_Voucher,statistics_Vouchers,statistics_Voucher_Register,statistics_Accounts
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def Index(request):
   
    return render(request,'index.html')

def base(request):
    voucher =statistics_Vouchers.objects.all().order_by('Vouchers_name')
    return render(request, 'base.html',{'voucher':voucher})


def Statistics(request):
    voucher =statistics_Vouchers.objects.all().order_by('Vouchers_name')
    accounts = statistics_Accounts.objects.all()
    sum=0
    total1= statistics_Total_Voucher.objects.all()
    for i in total1:
        if i.Total:
            sum+=i.Total


    context = {
        
        'voucher':voucher,
        'sum':sum,
        'accounts':accounts,
        
        

    }

    
    return render(request,'statics.html',context)

def month(request,id):
    mo = Months.objects.all()

    vch = statistics_Vouchers.objects.get(id=id)
    count = statistics_Voucher_count.objects.filter(Voucher=id)
    total=0
    for i in count:
        if i.Total_Voucher:
            total+=i.Total_Voucher

    if statistics_Total_Voucher.objects.filter(Voucher=id):
        to=statistics_Total_Voucher.objects.get(Voucher=id)
        to.Voucher=vch
        to.Total=total
        to.save()
    else:
        to=statistics_Total_Voucher()
        to.Voucher=vch
        to.Total=total
        to.save()
   


    context = {
        'mo':mo,
        'vch':vch,
        'count':count,
        
        
        
        
        

    }

    
    return render(request,'month.html',context)



def Statistics_voucher_register(request,id,pk):
    voucher = statistics_Voucher_Register.objects.filter(Month=id,Voucher=pk)
    vch = statistics_Vouchers.objects.get(id=pk)
    

    total_debit=0
    total_credit=0

    for i in voucher:
        if i.Debit_Amount:
            total_debit +=i.Debit_Amount
        if i.Credit_Amount:
            total_credit +=i.Credit_Amount
    v=statistics_Vouchers.objects.get(id=pk)
    m=Months.objects.get(id=id)
    count = voucher.count()
    if statistics_Voucher_count.objects.filter(Month=id,Voucher=pk):
        total= statistics_Voucher_count.objects.get(Month=id,Voucher=pk)
        
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()
    else:
        total= statistics_Voucher_count()
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()


    context = {
        'voucher':voucher,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'vch':vch,
        'm':m,

        
        
        

    }

    
    return render(request,'voucher.html',context)



def Statistics_voucher_Delete(request,id,pk,de):
    voucher = statistics_Voucher_Register.objects.get(id=de)
    voucher.delete()
    return redirect(Statistics_voucher_register,id,pk)










def changecompany(request):
    return render(request, 'changecompany.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Compony added successfully!")
        
        return redirect('/')

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')



