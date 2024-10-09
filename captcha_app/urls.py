from django.urls import path, include
from .views import GenerateCaptchaView, ValidateCaptchaView

urlpatterns = [
    path('generate/', GenerateCaptchaView.as_view(), name='generate_captcha'),
    path('validate/', ValidateCaptchaView.as_view(), name='validate_captcha'),

]
