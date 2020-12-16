from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'ticket'
urlpatterns = [                   
    path('dashboard',view=views.dashboard, name='dashboard'),
    path('create',view=views.create, name='create'),
    path('edit/<str:id>',view=views.edit, name='edit'),
    # ajax
    path('store',view=views.store, name='store'),
    path('get_tickets',view=views.get_tickets, name='get_tickets'),
    path('delete',view=views.delete, name='delete'),
    
]