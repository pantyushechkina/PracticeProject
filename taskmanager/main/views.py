from django.shortcuts import render, redirect
from .models import Contact, TypeProduct, Item


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    contactsList = Contact.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contactsList})


def catalog(request):
    items = Item.objects.all()
    categories = TypeProduct.objects.all()
    return  render(request, 'main/catalog.html', {'categories': categories, 'items': items})

