from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, \
    IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.token import account_activation_token
from apps.accounts.permissions import IsSelfOrAdminOrReadOnly
from apps.accounts.email import send_success_confirmation_email
from .serializers import SelfUserSerializer, \
    FullUserSerializer, \
    OtherUserSerializer

# Auth user model class
User = get_user_model()


@api_view(['GET'])
def activate_account(request, uidb64, token):
    """
    User account activation api view
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        send_success_confirmation_email(request, user)
        return Response(data={
            'success': 'Email successfully activated.'
        }, status=status.HTTP_200_OK)
    else:
        return Response(data={
            'failure': 'Link is no longer valid.'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(ListCreateAPIView):
    """
    API view which creates new user.
    """

    serializer_class = SelfUserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user and self.request.user.is_superuser:
            return FullUserSerializer
        return SelfUserSerializer


class UserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    API view which retrieve | update | delete user
    """

    serializer_class = SelfUserSerializer
    permission_classes = (IsAuthenticated,
                          IsSelfOrAdminOrReadOnly,)
    queryset = User.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return SelfUserSerializer
        if self.request.user.is_superuser:
            return FullUserSerializer
        return OtherUserSerializer
