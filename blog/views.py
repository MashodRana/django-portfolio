from django.shortcuts import render

from blog.models import PostModel, CategoryModel, CommentModel
from blog.forms import CommentForm


# Create your views here.
def post_view(request):
    posts = PostModel.objects.all().order_by('-created_on')
    context = {
        'title': 'Posts',
        'posts': posts
    }

    return render(request=request, template_name='blog/posts.html', context=context)

def post_detail_view(request, id):
    post = PostModel.objects.get(pk=id)
    
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentModel(
                author=form.cleaned_data.get('author'),
                body=form.cleaned_data.get('body'),
                post=post
            )
    
    comments = CommentModel.objects.filter(post=post)

    context = {
        'title': 'Post Detail',
        'post': post,
        'comments': comments
    }

    return render(request=request, template_name='blog/post_detail.html', context=context)

def post_category_view(request, category):
    posts = PostModel.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'title': 'Categorical Posts',
        'posts': posts
    }

    return render(request=request, template_name='blog/post_category.html', context=context)

