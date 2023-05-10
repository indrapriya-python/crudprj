from django.contrib import admin
from django.urls import path
from django.urls import include, re_path

from simpleform import views
urlpatterns = [
    path('',views.pro),
    path('create/',views.create),
    path('retrieve/', views.retrieve),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"), 
    path("update/<int:id>/", views.update, name="update"),
    path('update_data/',views.update_data), 

]
