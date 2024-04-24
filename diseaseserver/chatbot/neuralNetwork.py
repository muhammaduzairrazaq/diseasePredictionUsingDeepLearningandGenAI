import pickle
import pandas as pd
from .symptoms import *
# import symptoms as symp


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
            symptoms = self.encode_symptom(symptoms)
        with open('/home/iamblack/Documents/DiseasePrediction/diseasePredictionServerDjango/diseaseserver/chatbot/modertx.pkl', 'rb') as file:
            model = pickle.load(file)
        return disease_index[model.predict([symptoms])[0]]

    # get description of the predicted disease

    def disease_description(self, disease):
        df_description = pd.read_csv(
            "/home/iamblack/Documents/DiseasePrediction/diseasePredictionServerDjango/diseaseserver/chatbot/symptom_description.csv")
        return df_description[df_description['Disease'] == disease]['Description'].values[0]

    # get precautions of the predicted disease
    def disease_precaution(self, disease):
        df_precaution = pd.read_csv(
            "/home/iamblack/Documents/DiseasePrediction/diseasePredictionServerDjango/diseaseserver/chatbot/symptom_precaution.csv")
        return df_precaution[df_precaution['Disease'] == disease][:].values[0][1:].tolist()


# neural = NeuralNetwork()
# reported_symptoms = ['itching', 'skin rash', 'nodal skin eruptions',
#                      'continuous sneezing', 'shivering', 'chills', 'joint pain',]

# pred = neural.predict(reported_symptoms)
# print(f'Predicted Disease is {pred}')

# des = neural.disease_description(pred)
# print(f'Predicted Disease Description {des}')

# prec = neural.disease_precaution(pred)
# print(f'Predicted Disease Precautions {prec}')
