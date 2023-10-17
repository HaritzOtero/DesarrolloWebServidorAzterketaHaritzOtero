from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('pertsonak/', views.pertsonak, name='add'),
    path ('pertsonak/aldatuPertsona/<int:id>/aldatuPertsonaEtxea/', views.aldatuPertsonaEtxea, name='add'),
    path ('pertsonak/aldatuPertsona/<int:id>/', views.aldatuPertsona, name='add'),
    path ('add/', views.add, name='add'),
    path ('add/addetxea/', views.addEtxea, name='addpost'),
    path ('ezabatu/', views.deleteEtxea, name='ezabatu'),
    path ('ezabatu/<int:id>/', views.deleteEtxea, name='ezabatu'),
    path ('pertsonak/ezabatuPertsona/<int:id>/', views.deletePertsona, name='ezabatu'),
    path ('aldatu/<int:id>/', views.aldatu),
    path ('aldatuEtxea/<int:id>/', views.aldatuEtxea),
    path ('pertsonak/addPertsona/', views.addPertsona, name='addAuthor'),
    path ('pertsonak/addPertsona/addEtxeaPertsona/', views.addEtxeaPertsona, name='addpostAuthor'),
 
    

]