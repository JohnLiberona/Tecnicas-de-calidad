from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Persona

        
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido']


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()


    def create(self, data):
        user = user()
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.username = data.get('username')
        user.email = data.get('email')
        user.set_password (data.get('password'))
        user.save()
        return user
    

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users)!=0:
            return serializers.ValidationError("El usuario ya existe, por favor. Ingrese otro usuario.")
        else:
            return data