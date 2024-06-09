import pandas as pd
import numpy as np
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras
from .symptoms import *

class NeuralNetwork:

    # one hot encoding symptoms
    def encode_symptom(self, symptoms):
        # Initialize the output list with zeros
        symptoms_binary = [0] * 132
        # Map reported symptoms to binary representation
        for symptom in symptoms:
            if symptom in symptom_dataset:
                index = symptom_dataset.index(symptom)
                symptoms_binary[index] = 1
        return symptoms_binary

    # loading the model and making prediction
    def predict(self, symptoms, encode=True):
        if encode:
            symptoms_binary = self.encode_symptom(symptoms)
        input_symptoms = np.array([symptoms_binary]).astype(np.float32)
        model = load_model(r'C:\Users\PMLS\Documents\Disease Prediction\diseasePredictionServerDjango\diseaseserver\chatbot\neural_network.h5')
        prediction = model.predict(input_symptoms)
        class_prediction = np.argmax(prediction, axis=1)
        predicted_disease = list(disease_index.keys())[list(disease_index.values()).index(class_prediction[0])]
        return predicted_disease

    # get description of the predicted disease

    def disease_description(self, disease):
        df_description = pd.read_csv(
            r"C:\Users\PMLS\Documents\Disease Prediction\diseasePredictionServerDjango\diseaseserver\chatbot\symptom_description.csv")
        return df_description[df_description['Disease'] == disease.strip()]['Description'].values[0]

    # get precautions of the predicted disease
    def disease_precaution(self, disease):
        df_precaution = pd.read_csv(
            r"C:\Users\PMLS\Documents\Disease Prediction\diseasePredictionServerDjango\diseaseserver\chatbot\symptom_precaution.csv")
        return df_precaution[df_precaution['Disease'] == disease.strip()][:].values[0][1:].tolist()


# testing
# neural = NeuralNetwork()
# reported_symptoms = ['high fever', 'runny nose', 'chills']

# pred = neural.predict(reported_symptoms)
# print(f'Predicted Disease is {pred}')
# des = neural.disease_description(pred)
# print(f'Predicted Disease Description {des}')

# prec = neural.disease_precaution(pred)
# print(f'Predicted Disease Precautions {prec}')
# for pred in disease_index.keys():
#     try:
#         print(f'Predicted Disease is {pred}')
#         des = neural.disease_description(pred)
#         print(f'Predicted Disease Description {des}')

#         prec = neural.disease_precaution(pred)
#         print(f'Predicted Disease Precautions {prec}')
#     except:
#         print(f'Error in {pred}')
#         break
 
    
