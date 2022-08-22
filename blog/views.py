from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.
def post_list(request):
    '''post list 视图方法，返回已发布所有posts'''
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post, year, month, day):
    '''post detail 视图，返回请求条件相符合的Post'''
    posts = get_object_or_404(Post, slug = post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'posts' : posts})