

from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_login, name="admin_login"),
    path('home', views.index, name="home"),

    # Admin...
    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_register', views.admin_register, name="admin_register"),
    path('admin_list', views.admin_list, name="admin_list"),
    path('delete_admin', views.delete_admin, name="delete_admin"),

    # Books...
    path('add_book', views.add_book, name="add_book"),
    path('edit_book', views.edit_book, name="edit_book"),
    path('delete_book', views.delete_book, name="delete_book"),
]