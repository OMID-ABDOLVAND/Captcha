from django.apps import AppConfig


class CaptchaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'captcha_app'

    def ready(self):
        import captcha_app.signals