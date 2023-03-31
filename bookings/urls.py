from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('', views.index, name='main_page'),
    path('book/', views.book, name='book_page'),
    path('check_available_tables/', views.check_available_tables, name='tables_API',)
]