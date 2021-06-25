from django.shortcuts import render
from .models import Post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    all_posts = Paginator(Post.objects.all(),3)
    page = request.GET.get('page')
    try:
        posts = all_posts.page(page)
    except PageNotAnInteger:
        posts = all_posts.page(1)
    except EmptyPage:
        posts = all_posts.page(all_posts.num_pages)
        
    
    
    params = {
        'posts' : posts,
        'posts_lat' : Post.objects.all(),
        'category' : Category.objects.all(),
    }
    return render(request, 'index.html',params)
