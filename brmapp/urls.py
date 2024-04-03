from django.urls import path
from .views import helloView,addBookView,addBook,editBook,editBookView,deleteBookView

urlpatterns = [
    path("",helloView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView)
]
