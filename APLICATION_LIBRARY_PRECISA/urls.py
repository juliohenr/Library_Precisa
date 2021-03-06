from django.urls import path
from . import views

urlpatterns = [
    path('get_books',views.get_books,name='get_books'),
    path('add_books',views.add_books,name='add_books'),
    path('delete_books',views.delete_books,name='delete_books'),
    path('update_books',views.update_books,name='update_books'),
    path('test_binary',views.test_binary,name='test_binary'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('search_results',views.search_results,name='search_results'),
    path('results',views.results,name='results'),
    path('read_more',views.read_more,name='read_more'),
    path('persist_read_more',views.persist_read_more,name='persist_read_more'),
    path('',views.index,name='index'),
]

