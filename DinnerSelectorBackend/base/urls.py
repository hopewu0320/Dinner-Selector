from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('dinner-option/', views.my_view),
    path('dinner-option/', views.pickupDinner),
]
