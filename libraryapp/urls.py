from django.urls import path
from .views import BookListApi,book_list_view,BookRetrieveApiView,BookDestroyApiView,BookUpdateApiView, BookViewsSet
from .views import BookCreateApiView,BookListCreateApiView,BookUpdateDeleteApiView
from rest_framework.routers import SimpleRouter 


router = SimpleRouter()
router.register('books', BookViewsSet, basename='books')

urlpatterns = [
    # path('books/', BookListApi.as_view()),
    # path('books/<int:pk>/', BookRetrieveApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDestroyApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/create/',BookCreateApiView.as_view()),
    # path('bookslistcreate/',BookListCreateApiView.as_view()),
    # path('booksupdatedelete/<int:pk>/',BookUpdateDeleteApiView.as_view()),
    # path('books2/', book_list_view),
    
    
]


urlpatterns += urlpatterns + router.urls