from django.urls import path
from .views import GoogleLoginView,CustomTokenRefreshView

urlpatterns = [
    path("api/google-login/", GoogleLoginView.as_view(), name='google-login'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
