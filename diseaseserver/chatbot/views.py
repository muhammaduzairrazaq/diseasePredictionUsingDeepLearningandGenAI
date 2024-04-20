from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .adax import Adax
import time

adax = Adax()

class ReactView(APIView):
    def post(self, request):
        query = request.data.get('query', '')
        # passing the query to chatbot
        # response = adax.chat(query)
        time.sleep(2)
        response = 'hello i got you baby...'
        return Response(response)
