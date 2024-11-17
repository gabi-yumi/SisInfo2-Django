from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, CategoryDetailView, CategoryListView, CommentCreateView, SearchBooksView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
    path('search/', SearchBooksView.as_view(), name='search'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
     path('categorias/', CategoryListView.as_view(), name='category_list'),
    path('categoria/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]

