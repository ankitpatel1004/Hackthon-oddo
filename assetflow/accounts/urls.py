# pyrefly: ignore [missing-import]
from django.urls import path
# pyrefly: ignore [missing-import]
from accounts.views import *

urlpatterns = [
    path("login",user_login,name="login"),
    path("signup",user_signup,name="signup"),
    path('forgotpassword',forgot_password,name="forgotpassword"),
    path('reset_password',reset_password,name="reset_password"),
    path('password_success',password_success,name="password_success")
]
