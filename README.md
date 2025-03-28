# Healthcare AI System

## Project Overview
This project is an AI-powered healthcare system designed to assist users in diagnosing diseases and understanding their medical reports. It utilizes advanced deep learning and retrieval-augmented generation (RAG) techniques to enhance medical analysis and patient support.

## Technologies Used
- **Python**
- **LangChain**  
- **ChromaDB**
- **TensorFlow**
- **Unsloth**
- **Hugging Face Transformers**
- **FAISS**
- **RESTAPI**

## Features
### 🔹 Disease Prediction
- Users enter their symptoms, and the neural network predicts the most likely disease.
- Voice-based input for seamless interaction.
- Model trained on extensive medical datasets to achieve high accuracy.

### 🔹 Symptom Retrieval using LLM
- Google Gemma 2B model fine-tuned on doctor-patient interactions.
- Helps in mapping user input to precise medical symptoms.

### 🔹 RAG-based Medical Report Analysis
- Users can upload medical reports (PDFs, images, or text files).
- AI processes and retrieves relevant medical information.
- Users can chat with the AI to understand their reports better.

## Model Details
- **Neural Network**: Multi-layer deep learning model trained on medical datasets.
- **Fine-Tuned Google Gemma 2B**: Optimized for medical symptom retrieval.
- **RAG Implementation**: Uses ChromaDB for document retrieval and meta llm for response generation.

## Future Improvements
- Enhance dataset diversity for better generalization.
- Expand disease coverage beyond 130 illnesses.


