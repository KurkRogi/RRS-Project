from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('', views.index, name='main_page'),
    path('book/', views.book, name='book_page'),
    path('check_available_tables/', views.check_available_tables, name='tables_API',),
    path('edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:id>/', views.delete_booking, name='delete_booking'),
]