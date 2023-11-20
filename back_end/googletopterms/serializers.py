from rest_framework import serializers
from .models import queries, comment
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value: str) -> str:
        validate_password(value)
        return value

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)  # Asigna y hashea la contraseña
            user.save()
            Token.objects.create(user=user)  # Crea un token para el usuario
        return user

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'token': instance.auth_token.key,
        }


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('comment', 'user', 'query')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'comment': instance.comment,
            'username': instance.user.username,
        }


class queriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = queries
        fields = ('id',
                  'name',
                  'description',
                  'rawQuery',
                  'relatedTo',
                  'public',
                  'user',
                  'comments')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'rawQuery': instance.rawQuery,
            'relatedTo': instance.relatedTo,
            'username': instance.user.username,
            'comments': commentSerializer(instance.comments.all(), many=True).data,
        }
