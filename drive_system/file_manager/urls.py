from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('file_list/', views.file_list, name='file_list'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('create_file/', views.create_file, name='create_file'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),

]
