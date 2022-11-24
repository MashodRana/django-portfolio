from django.shortcuts import render

from blog.models import PostModel, CategoryModel, CommentModel
from blog.forms import CommentForm, PostForm


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
    print(request.user)
    print(request.user.username)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentModel(
                author=str(request.user.username),
                body=form.cleaned_data.get('body'),
                post=post
            )
            comment.save()
    
    comments = CommentModel.objects.filter(post=post)
    for com in comments:
        print(com.author)
        print(com.body)
        print()

    context = {
        'title': 'Post Detail',
        'post': post,
        'comments': comments,
        'form': CommentForm()
    }

    return render(request=request, template_name='blog/post_detail.html', context=context)

def post_add_view(request):
    print("I am in the post add view")
    form = PostForm()
    if request.method=='POST':
        pass
    context = {
        'title': 'Add new post',
        'form': form,
    }
    print("I am here........")
    return render(request=request, template_name='blog/post_add.html', context=context)



def post_category_view(request, category):
    posts = PostModel.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'title': 'Categorical Posts',
        'posts': posts
    }

    return render(request=request, template_name='blog/post_category.html', context=context)

