from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyAssets

def get(request):
    params = {}
    if request.method == 'GET':
        item_name = request.GET.get('itemName')
        if item_name is not None:
            result = CompanyAssets.objects.filter(item_name__icontains=item_name)
        else:
            result = CompanyAssets.objects.all()
        context = {
            'result': result,
            'item_name' : item_name
        }
    return render(request, 'search_result.html', context)
