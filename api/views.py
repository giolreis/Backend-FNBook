from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post

from django.http import JsonResponse
from api.models import MyModel
from django.db import connection

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all().values()
    return Response(posts)

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")  # Testa a conexão ao banco de dados
        return JsonResponse({"status": "success", "message": "Conexão bem-sucedida!"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    

def register_user(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Verifica se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email já cadastrado'}, status=400)

        # Cria o usuário
        user = User.objects.create(
            username=email,  # Usa o email como username
            email=email,
            first_name=name,
            password=make_password(password)
        )
        return JsonResponse({'message': 'Usuário criado com sucesso!'}, status=201)
    return JsonResponse({'error': 'Método não permitido'}, status=405)


def login_user(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'Login realizado com sucesso!'})
        return JsonResponse({'error': 'Credenciais inválidas'}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)
