from django.urls import path

from blog import views


urlpatterns = [
    path('', views.post_view, name='posts' ),
    path('<int:id>/', views.post_detail_view, name='post_detail'),
    path("<category>/", views.post_category_view, name='post_category'),
]