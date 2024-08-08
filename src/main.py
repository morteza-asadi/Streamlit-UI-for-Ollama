from typing import List 
import streamlit as st
import ollama

from chat_history import ChatHistory
from chat_ui import ChatUI
from ollama_chat_model import OllamaChatModel 

PROJECT_NAME = "Simple Ollama Streamlit UI"

def load_models() -> List[str]:
    models = [model["name"] for model in ollama.list()["models"]]
    return models

def main():
    st.set_page_config(page_title=PROJECT_NAME, page_icon="🤖")
    st.title(PROJECT_NAME)

    models = load_models()
    
    selected_model = st.selectbox("Select your Model:", models)

    chat_model = OllamaChatModel(selected_model)
    
    chat_history = ChatHistory()
    
    chat_ui = ChatUI(chat_model, chat_history)
    chat_ui.render()

if __name__ == "__main__":
    main()