from django.urls import path
from .views import get_posts, register_user
from . import views
from .views import register_user, login_user 

urlpatterns = [
    path('posts/', get_posts),
    path('test-db/', views.test_db_connection, name='test_db_connection'),
    path('register/', register_user, name='register'),  # Rota para criar uma conta
    path('login/', login_user, name='login'),          # Rota para login
]
