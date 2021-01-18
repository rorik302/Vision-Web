from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
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

        current_site = get_current_site(request)
        verification_url = reverse('verification')

        send_mail(
            subject='Активация аккаунта',
            message=f'Для активации аккаунта перейдите по ссылке: \n'
                    f'http://{current_site.domain}{verification_url}?uuid={client.uuid}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email],
            fail_silently=False,
        )

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def verification(self, request, *args, **kwargs):
        uuid = request.query_params['uuid']
        client = client_model.objects.filter(uuid=uuid).first()
        if client:
            client.is_active = True
            client.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
