from django.shortcuts import render

from blog.models import PostModel, CategoryModel, CommentModel


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
    context = {
        'title': 'Post Detail',
        'post': post
    }

    return render(request=request, template_name='blog/post_detail.html', context=context)

def post_category_view(request, category):
    posts = PostModel.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'title': 'Categorical Posts',
        'posts': posts
    }

    return render(request=request, template_name='blog/post_category.html', context=context)

