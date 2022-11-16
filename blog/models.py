from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    """Store category of post."""
    name = models.CharField(max_length=31)


class PostModel(models.Model):
    """ Store post details information """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(CategoryModel, related_name='posts')


class CommentModel(models.Model):
    author = models.CharField(max_length=63)