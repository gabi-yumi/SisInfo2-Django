from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from books.form import PostForm
from books.models import Category, Comment, Post

class BookListView(ListView):
    model = Post
    template_name = 'books/index.html'
    context_object_name = 'book_list'


class BookCreateView(CreateView):
    model = Post
    form_class = PostForm  
    template_name = 'books/create.html'

    def get_success_url(self):
        return reverse('books:detail', args=[self.object.pk])

class BookUpdateView(UpdateView):
    model = Post
    fields = ['title', 'release_year', 'content', 'poster_url']
    template_name = 'books/edit.html'
    context_object_name = 'book'

    def get_success_url(self):
        return reverse('books:detail', kwargs={'pk': self.object.pk})

class BookDeleteView(DeleteView):
    model = Post
    template_name = 'books/delete_confirm.html'
    context_object_name = 'book'
    success_url = reverse_lazy('books:index')

class SearchBooksView(ListView):
    model = Post
    template_name = 'books/search.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.none()

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'books/comment_form.html'
    fields = ['text']  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])  
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])  
        return context

    def get_success_url(self):
        return reverse('books:detail', kwargs={'pk': self.object.post.pk})


class BookDetailView(DetailView):
    model = Post
    template_name = 'books/detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'books/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'books/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()
        return context
    

    

