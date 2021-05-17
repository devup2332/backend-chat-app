
from django.urls.conf import path
from rest_framework_simplejwt.views import TokenVerifyView
from api import views

urlpatterns = [
    path("auth/login",views.LoginView.as_view()),
    path("auth/verify",TokenVerifyView.as_view()),
    path("messages",views.MessageView.as_view()),
    path("auth/register",views.RegisterView.as_view()),
    path("auth/validate-email/<str:email>",views.ValidateEmailView.as_view())
]

