from django.forms import ModelForm

from blog.models import CommentModel


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['author', 'body']