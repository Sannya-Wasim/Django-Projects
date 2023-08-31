from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members')
    path('employees/', views.employees, name='index'),
    path('form/', views.form, name='form')
]