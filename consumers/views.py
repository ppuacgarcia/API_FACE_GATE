from django.http import JsonResponse
from django.shortcuts import render, redirect

from utils.recognition import Recognition
from .models import MyUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from graphql_jwt.decorators import permission_required
from django.contrib import messages
import requests

def user_list(request):
    users = MyUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

User = get_user_model()

def create_user(request):
    if request.method == 'POST':
        # Recibe los datos del formulario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            messages.info(request,"El usuario ya existe")
            return render(request, 'create_user.html')

        # Llama a la mutación de GraphQL
        mutation = '''
            mutation createUser {
                createUser(
                    email: "%s",
                    firstName: "%s",
                    lastName: "%s",
                    password: "%s",
                    username: "%s",
                    videoPath:""
                ) {
                    user{
                        id
                        isSuperuser
                        isStaff
                        isActive
                        dateJoined
                        lastLogin
                        username
                        firstName
                        lastName
                        email
                    }
                }
            }
        ''' % (email, first_name, last_name, password, username)

        response = requests.post('http://localhost:8000/graphql/', json={'query': mutation})
        # Verifica si la mutación fue exitosa
        if response.status_code == 200:
            data = response.json()
            user_data = data.get('data', {}).get('createUser', {}).get('user', {})
            return redirect('user_list.html')
        else:
            messages.error(request, 'Error al crear el usuario')
            return render(request, 'create_user.html')
    else:
        # Renderiza el template HTML
        return render(request, 'create_user.html')

def recognize_face(request):
    try:
        # Devolver la respuesta JSON con el resultado del reconocimiento
        return Recognition.face_recognizer('./data')
    except Exception as e:
        # En caso de cualquier error, devolver un mensaje de error
        return JsonResponse({'error': str(e)}, status=500)
    