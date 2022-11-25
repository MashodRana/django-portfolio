from django.urls import path

from blog import views


urlpatterns = [
    path('', views.post_view, name='posts' ),
    path('<int:id>/', views.post_detail_view, name='post_detail'),
    path("add/", views.post_add_view, name='post_add'),
    path("delete/<int:id>/", views.post_delete_view, name='post_delete'),
    path("<category>/", views.post_category_view, name='post_category'),
    
]