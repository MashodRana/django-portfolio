from django.contrib import admin

from blog.models import PostModel, CategoryModel


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostModel, PostAdmin)
admin.site.register(CategoryModel, CategoryAdmin)