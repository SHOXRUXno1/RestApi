from django.urls import path

from .views import BookListApiView, BookDetailApiView, BookCreateApiView, \
    BookUpdateApiView,BookDeleteApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), ),
    path('books/create/', BookCreateApiView.as_view(), ),
    path('books/<int:pk>/', BookDetailApiView.as_view(), ),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(), ),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), ),
]
