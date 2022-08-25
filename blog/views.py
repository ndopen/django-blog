from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

from .models import Post, Comment

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

    # list of active comment for the this post
    comments = posts.comments.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = posts
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'posts' : posts, 'comments':comments, 'new_comment': new_comment, 'comment_form': comment_form})

def post_share(request, post_id):
    '''post in email share'''
    # 通过id检索post
    post = get_object_or_404(Post, id=post_id, status = 'published')
    sent = False

    if request.method == 'POST':
        # 提交form
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 表单域已通过验证
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent})