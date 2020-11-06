from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #Django Admin
    path('admin/',admin.site.urls),
    
    #User Management
    path('accounts/',include('django.contrib.auth.urls')),


    #Local Apps
    path('accounts/',include('users.urls') ),
    path('',include('pages.urls')),

]

