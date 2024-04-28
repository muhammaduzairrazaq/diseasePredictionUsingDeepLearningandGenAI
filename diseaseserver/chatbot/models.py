from django.db import models
import json
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    @classmethod
    def delete_account(cls, email):
        try:
            print(email)
            user = cls.objects.get(email=email)
            user.delete()
            return {'message': 'Account deleted successfully'}
        except ObjectDoesNotExist:
            return {'error': 'User with the provided email does not exist'}, status.HTTP_404_NOT_FOUND
        except Exception as e:
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR


class DiseaseReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    positive_symptoms = models.TextField()
    negative_symptoms = models.TextField()
    precautions = models.TextField()
    description = models.TextField(default="None")
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def add_disease_report(cls, user, disease_name, positive_symptoms, negative_symptoms, precautions, description):
        # Convert Python lists to JSON strings
        positive_symptoms_json = json.dumps(positive_symptoms)
        negative_symptoms_json = json.dumps(negative_symptoms)
        precautions_json = json.dumps(precautions)

        # Create a new DiseaseReport instance
        cls.objects.create(
            user=user,
            disease_name=disease_name,
            positive_symptoms=positive_symptoms_json,
            negative_symptoms=negative_symptoms_json,
            precautions=precautions_json,
            description=description
        )
        
    @classmethod
    def get_disease_reports(cls, email):
        # Get the user instance
        user = User.objects.get(email=email)
        # Get all DiseaseReport instances related to the user
        reports = cls.objects.filter(user=user)
        # Create a list to store attributes
        report_list = []
        # Iterate over each report and append its attributes to the list
        for report in reports:
            attributes = {
                "report_id": report.id,
                "user": report.user.email,
                "disease_name": report.disease_name,
                "positive_symptoms": json.loads(report.positive_symptoms),
                "negative_symptoms": json.loads(report.negative_symptoms),
                "precautions": json.loads(report.precautions),
                "description": report.description,
                "date": report.date.strftime("%Y-%m-%d %H:%M:%S")
            }
            report_list.append(attributes)
        print(report_list)
        return report_list
    
    @classmethod
    def delete_disease_reports(cls, report_id):
        try:
            # Try to retrieve the report
            report = cls.objects.get(id=report_id)
        except cls.DoesNotExist:
            # If the report does not exist, return an error response
            return {'error': 'Report with the provided ID does not exist'}, status.HTTP_404_NOT_FOUND
        except Exception as e:
            # Handle other unexpected errors
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR

        # If the report exists, delete it
        try:
            report.delete()
            return {'message': 'Report deleted successfully'}, status.HTTP_200_OK
        except Exception as e:
            # Handle deletion errors
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR

