from ..utils.user_utils import user_authenticated
from rest_framework import generics, status
from googletopterms.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data["body"])
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)


class UserLoginView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = user_authenticated(request)
        if user is not None and user.is_active:
            # El usuario ha sido autenticado exitosamente
            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': user.username,
                             'token': token.key, 'message': 'Login successful'},
                            status=status.HTTP_200_OK)
        else:
            # Las credenciales son inválidas o el usuario no existe
            return Response({'message': 'invalid Credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)
