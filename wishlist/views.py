from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Aulia Satrio Wijoyo'
    }
    return render(request, "wishlist.html", context)

def show_barang(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")