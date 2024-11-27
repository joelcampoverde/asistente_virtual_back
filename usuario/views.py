# views.py
import os

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from django.conf import settings


# Create your views here.
class GoogleLoginView(APIView):
    permission_classes = [AllowAny]  # Permite acceso sin autenticación

    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Especifica el CLIENT_ID de tu aplicación de Google
            CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
            print(f"CLIENT_ID: {CLIENT_ID}")
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

            # El token es válido y puedes obtener la información del usuario
            email = idinfo.get('email')
            first_name = idinfo.get('given_name')
            last_name = idinfo.get('family_name')

            # Verifica si el usuario ya existe
            user, created = User.objects.get_or_create(email=email, defaults={
                'username': email,
                'first_name': first_name,
                'last_name': last_name,
            })

            # Genera tokens de acceso y refresco
            refresh = RefreshToken.for_user(user)

            # Retorna los tokens al frontend
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        except ValueError:
            # Token inválido
            return Response({'error': 'Token inválido.'}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden eliminar su cuenta

    def delete(self, request):
        try:
            # El usuario autenticado está en `request.user`
            user = request.user

            # Elimina al usuario
            user.delete()

            return Response({'message': 'Cuenta eliminada exitosamente.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Error al eliminar la cuenta: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)