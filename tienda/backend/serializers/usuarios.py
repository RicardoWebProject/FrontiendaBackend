from rest_framework import serializers
#Modelo
from ..models.usuarios import Usuario
#Token Rest Framework
from rest_framework.authtoken.models import Token

class UserSerializer (serializers.ModelSerializer):
    """
    Serializador para datos de usuario del sistema (no clientes)
    """
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_active']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def create(self, validated_data):
        user = Usuario(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        return user