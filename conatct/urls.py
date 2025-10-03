from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),

    path('adminhome/', views.admin_dashboard, name='admin_dashboard'),
    path('editcontact/<int:pk>/', views.edit_admin, name='edit_admin'),
    path('deletecontact/<int:pk>/', views.admin_delete, name='admin_delete'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile_view, name='profile'),

]
