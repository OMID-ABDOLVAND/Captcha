from rest_framework import serializers
from .models import Captcha, APIKey
from djoser.serializers import UserSerializer

class CaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captcha
        fields = ['captcha_id', 'image']


class CaptchaValidationSerializer(serializers.Serializer):
    captcha_id = serializers.CharField(required=True)
    user_input = serializers.CharField(required=True)

    def validate(self, data):
        captcha_id = data.get('captcha_id')
        user_input = data.get('user_input')

        try:
            captcha = Captcha.objects.get(captcha_id=captcha_id)
        except Captcha.DoesNotExist:
            raise serializers.ValidationError("Invalid CAPTCHA ID")

        if captcha.text != user_input:
            raise serializers.ValidationError("Incorrect CAPTCHA input")

        return data


class CustomUserSerializer(UserSerializer):
    apikey = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('apikey',)

    def get_apikey(self, obj):
        try:
            api_key = APIKey.objects.get(user=obj)  # Adjust this to match your model structure
            return api_key.key
        except APIKey.DoesNotExist:
            return None