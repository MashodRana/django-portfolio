from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    if request.method=='POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentModel(
                author=str(request.user.username),
                body=form.cleaned_data.get('body'),
                post=post
            )
            comment.save()
        
    
    comments = CommentModel.objects.filter(post=post)

    context = {
        'title': 'Post Detail',
        'post': post,
        'comments': comments,
        'form': CommentForm()
    }

    return render(request=request, template_name='blog/post_detail.html', context=context)


@login_required
def post_add_view(request):
    form = PostForm()

    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(request.user)
            form.instance.user = request.user
            # print(form.user)
            post = form.save()

            return redirect("post_detail",id=post.pk)
    context = {
        'title': 'Add new post',
        'form': form,
    }
    return render(request=request, template_name='blog/post_add.html', context=context)

@login_required
def post_update_view(request, id):
    obj = get_object_or_404(PostModel, pk=id)

    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("post_detail", id=id)

    context = {
        'title': 'Update Post',
        'form': form,
        'categories_indices': ";".join([str(kv['id']) for kv in obj.categories.values()])
    }

    return render(request=request, template_name='blog/post_update.html', context=context)

@login_required
@require_POST
def post_delete_view(request, id):
    PostModel.objects.get(pk=id).delete()
    return redirect('posts')



def post_category_view(request, category):
    posts = PostModel.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'title': 'Categorical Posts',
        'posts': posts
    }

    return render(request=request, template_name='blog/post_category.html', context=context)

