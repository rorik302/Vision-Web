from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import serializers

client_model = get_user_model()


class AuthViewSet(GenericViewSet):
    queryset = client_model.objects.all()

    def get_serializer_class(self):
        if self.action == 'register':
            return serializers.ClientRegisterSerializer

    @action(methods=['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        client = client_model(email=serializer.validated_data['email'])
        client.set_password(serializer.validated_data['password'])
        client.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
