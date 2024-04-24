from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .adax import Adax
from .symptoms import *
import time

adax = Adax()


class ReactView(APIView):
    prev_session_id = previous_session_id

    def post(self, request):
        session_id = request.data.get('session_id')
        # self.prev_session_id = previous_session_id
        print(f'SESSION ID {session_id}')
        # print(f'PREVIOUS SESSION ID {self.prev_session_id}')
        if session_id == '1':
            # reset chat template
            print('RESETING CHAT')
            adax.reset()
        previous_session_id = session_id
        # print(f'PREVIOUS SESSION ID {previous_session_id}')
        query = request.data.get('query')
        query += " Note: Give me concise reply."
        # passing the query to chatbot
        response = adax.chat(query)
        if 'processing your reported symptoms' in response:
            if len(adax.reported_symptoms) <= 3:
                time.sleep(2)
                return Response('Please provide additional symptoms to enhance the accuracy of your diagnosis.')
            else:
                # initiate report generation
                dic = adax.disease_prediction()
                dic['response'] = response
                return JsonResponse(dic) 

        # time.sleep(2)
        # response = 'hello i got you baby...'
        # print(f'QUERY FROM USER: {query}')
        # print(f'RESPONSE GIVEN TO USER: {response}')
        dic = {'response': response}
        return JsonResponse(dic)
