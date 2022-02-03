
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('example/', views.example_view, name='example'),
    path('book_details/<int:pk_num>/', views.book_details, name='details'),
    path('book_details/<int:pk_num>/reviews/', views.book_details_reviews, name='details'),
]
