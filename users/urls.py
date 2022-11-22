from django.urls import path, include

from users import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='user_dashboard'),
]