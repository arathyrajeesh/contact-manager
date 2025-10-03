from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('adminhome/', views.admin_Dashboard, name='admin_dashboard'),
    path('deletecontact/<int:pk>/', views.admin_contact, name='admin_contact'),
    path('editcontact/<int:pk>/', views.edit_admin, name='edit_contact'),
    
    
]
