from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_barang
from wishlist.views import show_json
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_barang, name="show_barang"),
    path('json/', show_json, name="show_json"),
    path('json/<int:id>', show_json_by_id, name="show_json_by_id"),
]