from django.http import JsonResponse
from chatbot.models import *
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from .adax import Adax
from .clue import Clue
from .analyzereport import AnalyzeReport
from .symptoms import *
import time

adax = Adax()
clue = Clue()
analyzereport = AnalyzeReport()

# ngrok http --domain=pipefish-hip-aphid.ngrok-free.app 8000
# chroma run --path /db_path --port 5000


# View for user registration
class UserRegistrationView(APIView):
    def post(self, request):
        # Retrieve email and password from request data
        email = request.data.get('email')
        password = request.data.get('password')
        print(f'email {email}')
        print(f'password {password}')
        # Validate email and password
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        # Create user object
        try:
            user = User(email=email, password=password)
            user.save()
            return Response({'message': 'User account created successfully'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            print('error integrity.......')
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error.......')
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View for user verification


class UserVerificationView(APIView):
    def post(self, request):
        # Retrieve email and password from request data
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate email and password
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve user object
            user = User.objects.get(email=email)
            # Check if the provided password matches the stored password
            if password == user.password:
                return Response({'message': 'User account verified successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View for fetching disease reports


class DiseaseReportView(APIView):
    def post(self, request):
        # Retrieve email from request data
        email = request.data.get('email')

        # Validate email
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call get_all_attributes method to retrieve user attributes
            attributes_list = DiseaseReport.get_disease_reports(email)
            report = {}
            report['report_list'] = attributes_list
            # Set safe=False to allow serializing lists
            return JsonResponse(report, safe=False)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View for deleting disease reports


class DeleteReportView(APIView):
    def post(self, request):
        # Retrieve report_id from request data
        report_id = request.data.get('report_id')

        # Validate report id
        if not report_id:
            return Response({'error': 'Report ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call delete_disease_reports method to delete report
            response = DiseaseReport.delete_disease_reports(report_id)
            return JsonResponse(response)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View for deleting user account


class DeleteAccountView(APIView):
    def post(self, request):
        # Retrieve email id from request data
        email = request.data.get('email')

        # Validate email id
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call delete_disease_reports method to delete report
            response = User.delete_account(email)
            return JsonResponse(response)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# View for chat messages
class ReactView(APIView):
    def post(self, request):
        session_id = request.data.get('session_id')
        bot_name = request.data.get('bot')
        medical_report_data = request.data.get('reporttext')
        print('Reterived session id: ', session_id)
        email = request.data.get('email')
        if session_id == '1':
            # reset chat template
            print('RESETING CHAT')
            adax.reset()
        query = request.data.get('query').lower()

        # chating with Clue (gemma-2b-it finetunned) model

        if bot_name == "clue":
            response = clue.invoke_clue(query)
            dic = {'response': response}
            print(dic)
            return JsonResponse(dic)
        
        if bot_name == "areport":
            response = analyzereport.query_report(query, medical_report_data)
            dic = {'response': response}
            print(dic)
            return JsonResponse(dic)
        
        format_template = """
        Write a response without using bold words, headings, or list. \
        Dont use any symbols in your response like `<`, `>`, `%`, `$`, `&` `-`, `*` etc. \
        """
        query += f" Note: Don't provide all symptom suggestions at once. Follow the format while writing a reply ```{format_template}```"
        # passing the query to chatbot
        response = adax.chat(query)

        if 'okay, i\'m processing your reported symptoms. your report will be reviewed shortly.' in response.lower():
            if len(adax.reported_symptoms) <= 2:
                time.sleep(2)
                response = 'Please provide additional symptoms to enhance the accuracy of your diagnosis.'
                dic = {'response': response}
                return JsonResponse(dic)
            else:
                # initiate report generation
                user = User.objects.get(email=email)
                dic = adax.disease_prediction(user)
                dic['response'] = response
                return JsonResponse(dic)

        dic = {'response': response}
        print(dic)
        return JsonResponse(dic)
