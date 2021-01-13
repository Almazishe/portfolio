from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


# API's obtaining authorization functionalities to users | '/api/1.0.0/auth/<path>'
urlpatterns = [
    path('get-auth-token', obtain_auth_token, name='get-auth-token'),
    path('register', views.UserCreateView.as_view(), name='register-user'),
    path('user-account/<uuid>', views.UserRetrieveUpdateDeleteView.as_view(), name='rud-user'),
    path('user-account/activate/<uidb64>/<token>', views.activate_account, name='activate-user')
]
