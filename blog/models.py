from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    """Store category of post."""
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    """ Store post details information """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(CategoryModel, related_name='posts')

    def __str__(self) -> str:
        return self.title


class CommentModel(models.Model):
    """ Store post related comments. """
    author = models.CharField(max_length=63)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

