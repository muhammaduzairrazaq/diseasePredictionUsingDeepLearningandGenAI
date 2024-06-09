from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
TOGETHER_API_KEY = os.getenv('API_KEY')

class AnalyzeReport:
    def text_splitter(self, report_data):
        print('Initializing text splitter')
        character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=0
        )
        character_split_texts = character_splitter.split_text('\n\n'.join(report_data))

        # print(character_split_texts[5])
        # print(f"\nTotal chunks: {len(character_split_texts)}")

        token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, tokens_per_chunk=256)
        token_split_texts = []
        for text in character_split_texts:
            token_split_texts += token_splitter.split_text(text)

        # print(token_split_texts[5])
        # print(f"\nTotal chunks: {len(token_split_texts)}")

        return token_split_texts
    
    def chroma_db(self, token_split_texts, db_name="mderep"):
        print('Initializing chromadb')
        client = chromadb.PersistentClient(path="chroma") # setting up path where the chroma db will be stored
        chroma_client = chromadb.HttpClient(host='localhost', port=5000) # chroma server running on port 5000
        embedding_function = SentenceTransformerEmbeddingFunction()

        print(embedding_function([token_split_texts[5]]))
        try:
            chroma_client.delete_collection(name=db_name) # Delete a collection
            print('Previous collection deleted')
        except:
            pass
        chroma_collection = chroma_client.create_collection(db_name, embedding_function=embedding_function)

        ids = [str(i) for i in range(len(token_split_texts))]

        chroma_collection.add(ids=ids, documents=token_split_texts)
        print(f'Chroma collection count: ',chroma_collection.count())

        return  chroma_collection
    
    def rag(self, query, retrieved_documents):
        print('Initializing rag')
        information = "\n\n".join(retrieved_documents)
        client = Together(api_key=TOGETHER_API_KEY)
        response = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages = [
            {
                "role": "system",
                "content": """You are a helpful medical assistent. Your users are asking questions about their medical reports. \
                             You will be shown the user's question, and the relevant information from the medical report. \
                             Answer the user's question using only this information. If the user asks anything unrelated to health, respond with, "I am a medical bot and can't help you here" Don't answer such queries at any cost. \ """
            },
            {"role": "user", "content": f"Question: {query}. \n Information: {information}"}
        ]
        )
        content = (response.choices[0].message.content)
 
        return content or "Sorry try again!"
    
    def query_report(self, query, report_text):
        print(f'Report text {report_text}')
        print('Analyze report is activated')
        token_split_texts = self.text_splitter(report_text)
        chroma_collection = self.chroma_db(token_split_texts)

        results = chroma_collection.query(query_texts=[query], n_results=5)
        retrieved_documents = results['documents'][0]

        print('Reterived documents')
        for document in retrieved_documents:
            print('Document selected.')
            print(document)
            print('\n')
        
        response = self.rag(query, retrieved_documents)

        print(f'RAG response: {response}')
        return response
