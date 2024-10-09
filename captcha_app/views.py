import string
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import APIKeyAuthentication
from .models import Captcha
from .serializers import CaptchaSerializer, CaptchaValidationSerializer
from .utils import generate_captcha_text, generate_captcha_image
import random
# Create your views here.


class GenerateCaptchaView(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        captcha_text = generate_captcha_text()
        captcha_image = generate_captcha_image(captcha_text)
        captcha_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

        captcha = Captcha.objects.create(
            text=captcha_text,
            image=captcha_image,
            captcha_id=captcha_id,
            ip_address=request.META['REMOTE_ADDR']
        )

        serializer = CaptchaSerializer(captcha)
        return Response(serializer.data)


class ValidateCaptchaView(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CaptchaValidationSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({"success": True})
        else:
            return Response(serializer.errors, status=400)
