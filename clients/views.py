from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from . import serializers


class ClientListView(ListAPIView):
    serializer_class = serializers.ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        client_model = get_user_model()

        query = self.request.query_params

        if 'is_active' in query and query['is_active'].lower() == 'true':
            return client_model.objects.filter(is_active=True)

        return client_model.objects.all()
