from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdmin
from .serializers import (CreateTokenSerializer, CreateUserSerializer, UserSerializer)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    user.set_unusable_password()
    user.is_active = False
    user.save()
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'confirmation code',
        f'Confirmation code is: {confirmation_code}',
        f'donotreply@{settings.EMAIL_DOMAIN}',
        [user.email],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_token(request):
    serializer = CreateTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, email=serializer.validated_data['email'])
    request_code = serializer.validated_data['confirmation_code']
    if not default_token_generator.check_token(user, request_code):
        return Response(
            {'confirmation_code': request_code, 'detail': 'Conformation code is not valid'},
            status=status.HTTP_400_BAD_REQUEST
        )
    user.is_active = True
    user.save()
    token = AccessToken.for_user(user)
    return Response({'token': str(token)}, status=status.HTTP_200_OK)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    lookup_field = 'username'

    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
        else:
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=request.user.role, username=request.user.username, email=request.user.email)
        return Response(serializer.data, status=status.HTTP_200_OK)
