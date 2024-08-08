import streamlit as st
import ollama
from typing import List, Dict
from chat_model import ChatModel

class OllamaChatModel(ChatModel):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def stream_chat(self, messages: List[Dict[str, str]]) -> str:
        try:
            response = ''
            result = ollama.chat(
                model=self.model_name,
                messages=messages,
                stream=True  
            )
            with st.chat_message("ai"):
                with st.spinner("Writing ..."):
                    response_placeholder = st.empty()
                    for chunk in result:
                        response += chunk['message']['content']
                        response_placeholder.write(response)
            return response
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            return ""