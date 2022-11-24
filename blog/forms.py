from django.forms import ModelForm

from blog.models import CommentModel, PostModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        exclude = ['created_on', 'last_modified']

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['body']