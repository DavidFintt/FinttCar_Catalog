from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer


class usersApi(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        User = get_user_model()
        if self.request.user.is_superuser:
            queryset = User.objects.all()
        else:
            queryset = User.objects.filter(username=self.request.user.username)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            many=False
        )
        dealership = request.data['dealership']
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # def list(self, request, *args, **kwargs):
    #     users = self.get_queryset
    #     serializer = self.serializer_class(
    #         instance=users,
    #         many=True
    #     )
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)