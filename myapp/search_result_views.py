from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyAssets

def get(request):
    if request.method == 'GET':
        item_name = request.POST.get('itemName')
        jungle = request.POST.get('jungle')
        
