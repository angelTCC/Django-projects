from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='list'),
    path('create/', views.book_create, name='create'),
    path('delete/<int:pk>/', views.book_delete, name='delete'),
    path('edit/<int:book_id>/', views.book_edit, name='edit')
]
