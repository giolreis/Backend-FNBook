from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from api.views import login_user, register_user, test_db_connection

def home_view(request):
    return HttpResponse("Bem-vindo à API!")  # Mensagem simples para testar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home_view),  # Rota para a URL raiz
    path('test-db/', test_db_connection, name='test-db'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
