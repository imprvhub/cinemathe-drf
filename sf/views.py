# sf/views.py
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.http import HttpResponse

def index(request):
    """
    Displays an HTML page indicating the backend setup for Cinemathe.

    This function generates an HTML page with a heading and a paragraph indicating
    the backend setup for Cinemathe, along with the current time.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: An HTTP response with the generated HTML page.
    """
    html = f'''
    <html>
        <head>
            <title>Cinemathe - Django Rest Framework Backend</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }}
                .container {{
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                }}
                p {{
                    color: #666;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Cinemathe DRF Backend</h1>
                <p>This backend manages user authentication and registration for the Cinemathe app.</p>
                <p>Please visit the <a href="https://cinemathe-drf.vercel.app/admin">Django Admin panel</a> for backend management.</p>
                <p>For the frontend, visit <a href="https://cinemathe.netlify.app">Cinemathe</a>.</p>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name

        user.save()

        serializer = UserSerializer(user) 

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        
        return Response({'message': 'User registered successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'POST':
        print("POST request received.") 
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user) 
            refresh = RefreshToken.for_user(user)
            user_name = user.username
            user_email = user.email
            access_token = str(refresh.access_token)

            print("User authenticated successfully.") 
            return Response({'message': 'User authenticated successfully', 'username': user_name, 'email': user_email, 'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            print("Invalid credentials.")  
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        print("Method not allowed.")  
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        logout(request) 
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
