import time
from .symptoms import*
from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()
TOGETHER_API_KEY = os.getenv('API_KEY')


class Adax:
    user_messages = []

    client = OpenAI(
        api_key=TOGETHER_API_KEY,
        base_url='https://api.together.xyz/v1',
    )

    complete_args = {
        "messages": [
            {
                "role": "system",
                "content": f"""
            You are 'Adax,' a supportive medical assistant chatbot here to assist users with their symptoms. \
            Start with a professional greeting; you can use emojis. \
            Use maximum 20 words to write a reply . \
            If the user asks anything unrelated to health, respond with, "I am a medical bot and can't help you here" don't answere such query at any cost \
            Dont ask multiple questions in a single reply; just ask the most relevant question \
            When a user reports symptoms, ask if they have more symptoms to share. \
            Don't end the conversation until user ends it. \
            If the user indicates they've shared all their symptoms, respond with, "Okay, I'm processing \
            your reported symptoms. Your report will be reviewed shortly." Respect the user's decision. \
            Always maintain a professional tone. Your task is to engage users in conversation, \
            asking about their symptoms. Avoid sharing the user's message in your reply. """,
            }
        ],
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"

    }

    # calling the llm with user query
    def invoke_llm(self, prompt):
        self.complete_args['messages'].append(
            {'role': 'user', 'content': f"{prompt}"})
        chat_completion = self.client.chat.completions.create(
            **self.complete_args)
        self.complete_args['messages'].append(
            {'role': 'assistant', 'content': f"{chat_completion.choices[0].message.content}"})
        return chat_completion.choices[0].message.content

    # fetching symptoms from the user query to show symptoms suggestions
    def fetch_symptoms(self, query):
        symptom_selected = []
        words = query.split()
        for word in words:
            if len(word) >= 4:
                pattern = r".*" + word + r".*"
                for symptom in symptom_relation:
                    if re.match(pattern, symptom):
                        symptom_selected.extend(symptom_relation[symptom])
                        break
        return symptom_selected

    # validate_symptoms removing the symptoms from symptoms suggestion if it is already in the user query
    def validate_symptoms(self, query, symptoms):
        for symptom in symptom_dataset:
            if symptom in query:
                if symptom in symptoms:
                    symptoms.remove(symptom)
        return symptoms

    # conversation with chatbot
    def chat(self, query):
        query = query
        self.user_messages.append(query)
        symptoms = self.fetch_symptoms(query)

        if len(symptoms) > 0:
            symptoms = set(self.validate_symptoms(query, symptoms))

        prompt = query
        model_response = self.invoke_llm(prompt)

        # appending symptoms suggestion to the end of the model reply
        if len(symptoms) > 0:
            model_response += f' Do you have any of these symptoms {symptoms} if so reply with the symptom name.'

        # formatting the model response
        model_response = re.sub(r'.{0,5}:\s*', '', model_response)
        return model_response



if __name__ == '__main__':
    adax = Adax()
    while (True):
        query = input("Enter your query: ")
        if query == 'exit':
            break
        adax.chat(query)
