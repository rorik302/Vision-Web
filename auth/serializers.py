from django.contrib.auth import get_user_model
from rest_framework import serializers

client_model = get_user_model()


class ClientRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = client_model
        fields = ('email', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return attrs


class ClientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        if email is None:
            raise serializers.ValidationError('Необходимо ввести e-mail')
        if password is None:
            raise serializers.ValidationError('Необходимо ввести пароль')

        client = client_model.objects.filter(email=email).first()

        if not client:
            raise serializers.ValidationError({'email': 'Пользователь с таким e-mail не зарегистрирован'})

        if not client.is_active:
            raise serializers.ValidationError('Сначала необходимо активировать аккаунт')

        if not client.check_password(password):
            raise serializers.ValidationError({'password': 'Неверный пароль'})

        return attrs
