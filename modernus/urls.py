from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('appliances/', views.appliances, name="appliances"),
    path('login/', views.login, name="login"),
    path('sign-up/', views.signup, name="signup"),

    path('appliances/list/', views.admin_appliances, name='appliances_list'),
    path('appliances/add/', views.admin_appliances_add, name='appliances_add'),
    path('appliances/edit/<int:appliance_id>/', views.admin_appliances_edit, name='appliances_edit'),
    path('appliances/delete/<int:appliance_id>/', views.admin_appliances_delete, name='appliances_delete'),

    path('appliances/<int:appliance_id>/image/<int:image_id>/', views.admin_appliances_image_delete, name='image_delete'),
]