from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

class PostDetailView(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html' # название шаблона будет product.html
    context_object_name = 'post' # название объекта. в нём будет