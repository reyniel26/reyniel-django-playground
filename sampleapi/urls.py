from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_data),
    path('items/',views.get_items),
    path('add_item/',views.add_item)
]