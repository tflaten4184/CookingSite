from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import SignUpView

app_name = "accounts"

urlpatterns = [
    # path("", include("django.contrib.auth.urls"))
    # path('login/', auth_views.LoginView.as_view()),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', include("django.contrib.auth.urls")),

]
