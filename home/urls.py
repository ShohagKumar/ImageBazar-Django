
from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name='home'),
    path('', views.red, name='red'),
    path('catagory/<int:cid>', views.show_catagory, name='catagory'),
]
