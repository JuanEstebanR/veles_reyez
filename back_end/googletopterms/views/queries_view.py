from rest_framework import generics, status
from googletopterms.utils.user_utils import get_user_by_username
from googletopterms.models import queries
from googletopterms.serializers import queriesSerializer, commentSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json

# List all queries that are public for community
class QueriesAPIView(generics.ListAPIView):
    serializer_class = queriesSerializer

    def get_queryset(self):
        return queries.queriesObjects.all()


class MyQueriesAPIView(generics.ListCreateAPIView):
    serializer_class = queriesSerializer

    def get_queryset(self):
        # Obtener el nombre de usuario de la URL
        username = self.kwargs.get('username')
        # Obtener el objeto de usuario
        user = get_user_by_username(username)
        # Filtrar las consultas asociadas a ese usuario
        user_queries = queries.objects.filter(user=user)
        return user_queries

    def post(self, request, username=None, *args, **kwargs):
        data = json.loads(request.data["body"])
        username = data.get("username")
        user = get_user_by_username(username)
        mutable_data = data.copy()
        mutable_data['user'] = user.id
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QueriesDestroyAPIView(generics.DestroyAPIView):
    serializer_class = queriesSerializer

    def get_queryset(self):
        return queries.queriesObjects.all()

    def delete(self, request, pk=None, *args, **kwargs):
        query = self.get_queryset().filter(id=pk).first()
        if query:
            query.delete()
            return Response({'message': 'Query Deleted'},
                            status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = commentSerializer

    def get_queryset(self):
        return queries.queriesObjects.all()

    def post(self, request, pk=None, *args, **kwargs):
        query = self.get_queryset().filter(id=pk).first()
        if query:
            data = json.loads(request.data["body"])
            username = data.get("username")
            user = get_user_by_username(username)
            mutable_data = data.copy()
            mutable_data['query'] = query.id
            mutable_data['user'] = user.id
            serializer = self.get_serializer(data=mutable_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
