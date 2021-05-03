"""Account's module urls"""

from allauth.account.views import ConfirmEmailView, EmailVerificationSentView
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.urls import include, path

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("password-reset/", PasswordResetView.as_view()),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path(
        "registration/account-confirm-email/",
        EmailVerificationSentView.as_view(),
        name="account_email_verification_sent",
    ),
]
