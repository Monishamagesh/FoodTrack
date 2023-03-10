from django.urls import path
from .import views

urlpatterns=[
    path('',views.loadLogin),
    path('loadfood',views.loadFood, name='loadfood'),
    path('index',views.Index,name='Index'),
    path('addFood',views.addFood),
    path('userlogin',views.userlogin),
    path('delFood/<int:fid>',views.delFood,name="delFood")
]