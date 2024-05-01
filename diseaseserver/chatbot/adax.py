import time
from .symptoms import *
from .neuralNetwork import *
from chatbot.models import DiseaseReport
from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()
TOGETHER_API_KEY = os.getenv('API_KEY')


class Adax:
    def __init__(self):
        self.reported_symptoms = []
        self.suggested_symptoms = []
        self.client = OpenAI(
            api_key=TOGETHER_API_KEY,
            base_url='https://api.together.xyz/v1',
        )
        self.complete_args = {
            "messages": [
                {
                    "role": "system",
                    "content": f"""
            You are 'Adax', a supportive medical assistant chatbot here to help and assist users with their symptoms. \
            Don't use any words like I can't help you as it would depress the user. \
            Start with a professional greeting; you can use emojis. \
            If the user has entered symptoms in the query then look for related symptoms in this dataset {symptom_dataset} and fetch the related symptoms and give them as suggestions in your response. \
            Don't pass comments on disease diagnosis just try to get more symptoms from the user. \
            Don't provide any warnings that I can't provide diagnosis or consult a doctor the user already knows it. \
            If the user asks anything unrelated to health, respond with, "I am a medical bot and can't help you here" Don't answer such queries at any cost. \
            When a user reports symptoms, ask if they have more symptoms to share. \
            Don't end the conversation until the user ends it. \
            If the user indicates he has shared all his symptoms, then only respond with the message in backticks don't add anything else, \
            ```Okay, I'm processing your reported symptoms. Your report will be reviewed shortly.``` Respect the user's decision. \
            Always maintain a professional tone. Your task is to engage users in conversation, \
            asking about their symptoms. Avoid sharing the user's message in your reply. \
                """,
                }
            ],
            # "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"  # chat model
            "model": "meta-llama/Llama-3-70b-chat-hf"  # performing far better
        }

    # reset template for new conversation
    def reset(self):
        self.complete_args["messages"] = self.complete_args["messages"][:1]
        self.reported_symptoms = []
        self.suggested_symptoms = []

    # calling the llm with user query
    def invoke_llm(self, prompt):
        self.complete_args['messages'].append(
            {'role': 'user', 'content': f"{prompt}"})
        chat_completion = self.client.chat.completions.create(
            **self.complete_args)
        self.complete_args['messages'].append(
            {'role': 'assistant', 'content': f"{chat_completion.choices[0].message.content}"})
        return chat_completion.choices[0].message.content

    # fetch reported symptoms in the user query and store it
    def fetch_reported_symptoms(self, query, suggestion=False):
        for symptom in symptom_dataset:
            if symptom in query:
                if suggestion:
                    self.suggested_symptoms.append(symptom)
                    self.suggested_symptoms = set(self.suggested_symptoms)
                    self.suggested_symptoms = list(self.suggested_symptoms)
                else:
                    self.reported_symptoms.append(symptom)
                    self.reported_symptoms = set(self.reported_symptoms)
                    self.reported_symptoms = list(self.reported_symptoms)

    # initiating model to predict disease
    def disease_prediction(self, user):
        neural = NeuralNetwork()
        disease = neural.predict(self.reported_symptoms)
        description = neural.disease_description(disease)
        precaution = neural.disease_precaution(disease)
        if 'follow up' in precaution:
            precaution.remove('follow up')
        negative_symptoms = []
        for s in self.suggested_symptoms:
            if s not in self.reported_symptoms:
                negative_symptoms.append(s)
        if len(negative_symptoms) <= 0:
            negative_symptoms.append('None')

        symptoms = [str(s).title() for s in self.reported_symptoms]
        negativesymptoms = [str(s).title() for s in negative_symptoms]
        disease = str(disease).title()
        precaution = [str(p).capitalize() for p in precaution]
        description = str(description).capitalize()

        # Storing disease report in database
        DiseaseReport.add_disease_report(user=user, disease_name=disease, positive_symptoms=symptoms,
                                                  negative_symptoms=negativesymptoms, description=description, precautions=precaution)
        return {
            "symptoms": symptoms,
            "negativesymptoms": negativesymptoms,
            "disease": disease,
            "description": description,
            "precaution": precaution,
        }

    # conversation with chatbot
    def chat(self, query):
        if "shared all my symptoms" in query:
            time.sleep(2)
            print(f'REPORTED SYMPTOMS: {self.reported_symptoms}')
            return "Okay, I'm processing your reported symptoms. Your report will be reviewed shortly."
        self.fetch_reported_symptoms(query)
        print(f'REPORTED SYMPTOMS: {self.reported_symptoms}')
        model_response = self.invoke_llm(query)
        self.fetch_reported_symptoms(model_response, suggestion=True)
        pattern = r"(?:Confidence:|\(Note:).*"
        model_response = re.sub(pattern, "", model_response)
        return model_response


if __name__ == '__main__':
    adax = Adax()
    while (True):
        query = input("Enter your query: ")
        if query == 'exit':
            break
        print(adax.chat(query))
