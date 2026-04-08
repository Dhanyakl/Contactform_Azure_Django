from django.contrib import admin
from django.urls import path
from formsapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
] 
