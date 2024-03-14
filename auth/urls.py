from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from auth.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('sign_up', RegisterView.as_view(), name='sign_up'),
    path('sign_in', LoginView.as_view(), name='sign_in'),
    path('sign_out', LogoutView.as_view(), name='sign_out'),
]