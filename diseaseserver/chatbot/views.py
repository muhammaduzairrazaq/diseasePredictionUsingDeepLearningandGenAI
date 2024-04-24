from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .adax import Adax
from .symptoms import *
import time

adax = Adax()


class ReactView(APIView):
    def post(self, request):
        session_id = request.data.get('session_id')
        if session_id == '1':
            # reset chat template
            print('RESETING CHAT')
            adax.reset()
        query = request.data.get('query')
        format_template = """
        Write a response without using bold words, headings, list. \
        Use sentence case. \
        Dont use any symbols in your response like `<`, `>`, `%`, `$`, `&` `-`, `*` etc. \
        """
        query += f" Note: Give me concise reply. Don't provide all symptoms at once. Follow the format {format_template}"
        # passing the query to chatbot
        response = adax.chat(query)
            
        if 'Okay, I\'m processing your reported symptoms. Your report will be reviewed shortly.' in response:
            if len(adax.reported_symptoms) <= 3:
                time.sleep(2)
                response = 'Please provide additional symptoms to enhance the accuracy of your diagnosis.'
                dic = {'response': response}
                return JsonResponse(dic)
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
