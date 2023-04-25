from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    # path("", include("django.contrib.auth.urls"))
    # path('login/', auth_views.LoginView.as_view()),
    path('', include("django.contrib.auth.urls")),

]
