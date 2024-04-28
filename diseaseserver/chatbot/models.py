from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class DiseaseReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=100)
    positive_symptoms = models.TextField()
    negative_symptoms = models.TextField()
    precautions = models.TextField()
