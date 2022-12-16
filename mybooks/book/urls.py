from django.urls import path
from .views import * 

urlpatterns = [
    path("",Booklist),
    path("add/",post_book),
    path("update/<int:id>/",update_book),
    path("delete/<int:id>/",delete_book),
]