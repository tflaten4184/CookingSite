from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import SignUpView#, PasswordResetView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('', include("django.contrib.auth.urls")),
]
