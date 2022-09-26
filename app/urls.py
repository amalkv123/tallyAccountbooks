from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('changecompany',views.changecompany,name='changecompany'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtecompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('month',views.month,name='month'),
   
    






    
]