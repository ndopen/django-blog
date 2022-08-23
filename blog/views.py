from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post

# Create your views here.
def post_list(request):
    '''post list 视图方法 返回已发布所有posts'''
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页面不是整数，则传递第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页面超出范围，则提供最后一页的结果
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'posts' : posts, 'page':page})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, post, year, month, day):
    '''post detail 视图，返回请求条件相符合的Post'''
    posts = get_object_or_404(Post, slug = post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'posts' : posts})