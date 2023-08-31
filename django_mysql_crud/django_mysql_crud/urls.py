from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show', views.show),
    path('emp', views.emp),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('search/', views.search, name='search'),
]
