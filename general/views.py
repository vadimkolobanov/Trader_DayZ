import re

from django.shortcuts import render
from .models import *


def main_cover(request):
    context = {
        'name': 'some_text',
    }
    return render(request, 'pages/startpage.html', context)


def tabel_view(request):
    data = Item.objects.all()
    context = {
        'items': data
    }
    return render(request, 'pages/dashboard.html', context)


def trader_txt_import(request):
    traders = []
    categories = []
    items = []
    id_category = -1,
    with open('D:\\Python_Projects\\Trader_Dayz\\general\\tradef.txt', 'r', encoding='utf-8') as config:
        for i in config:

            values = i.strip()
            if values.startswith('<Trader>'):
                pass
                Trader.objects.create(name=values, owner_id=request.user.id)
                id_trader = Trader.objects.filter(name=values,owner_id=request.user.id).order_by('-id')[0].id
            elif values.startswith('<Category>'):
                pass
                Category.objects.create(name=values, attach_to_trader_id=id_trader, owner_id=request.user.id)
                id_category = Category.objects.filter(name=values, owner_id=request.user.id).order_by('-id')[0].id
            elif values.istitle():

                lst = values.replace('\t', '').split(',')
                print(lst)
                print(id_category)
                if len(lst) == 4:
                    Item.objects.create(class_name=lst[0], quantity=lst[1], buyvalue=int(lst[2]), sellvalue=int(lst[3]),
                                        owner_id=request.user.id, attach_to_category_id=id_category)

        print(traders)
    context = {
        'text': 'txt'
    }
    return render(request, 'pages/dashboard.html', context)
