from langchain_community.llms import Ollama
import time

class Clue:
    def invoke_clue(self, query='Hi, doc Clue i have pain in the stomach and i have high fever'):
        print('Clue being invoked.')
        start_time = time.time()
        llm = Ollama(model="Clue:latest")
        response = llm.invoke(query)
        end_time = time.time()
        print(response)
        print(f'Clue response time {end_time - start_time}')
        return response