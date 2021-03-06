from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import CompanyAssets

def index(request):
    return render(request, 'regist.html')

def create(request):
    if request.method == 'POST':
        item_name = request.POST.get('itemName')
        purchas_date = request.POST.get('purchaseDate')
        buyer = request.POST.get('buyer')
        jungle = request.POST.get('jungle')
        memo = request.POST.get('memo')
        company_assets = CompanyAssets(item_name = item_name,
            purchas_date = purchas_date,
            buyer = buyer,
            jungle = jungle,
            memo = memo,
            created_date = datetime.now(),
            updated_date = datetime.now())
        company_assets.save()
         
    params = {
        'result': '登録しました。',
    }
    return render(request, 'regist.html', params)
