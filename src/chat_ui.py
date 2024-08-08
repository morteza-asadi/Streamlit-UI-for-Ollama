import streamlit as st
from chat_model import ChatModel
from chat_history import ChatHistory

class ChatUI:
    def __init__(self, chat_model: ChatModel, chat_history: ChatHistory):
        self.chat_model = chat_model
        self.chat_history = chat_history

    def render(self):
        if st.button("Clear History", type="primary"):
            self.chat_history.clear_history()

        prompt = st.chat_input("Ask Anything")

        if prompt:
            self.chat_history.add_message("user", prompt)

            for message in self.chat_history.get_messages():
                with st.chat_message(message["role"]):
                    st.write(message["content"])

            response = self.chat_model.stream_chat(self.chat_history.get_messages())
            self.chat_history.add_message("assistant", response)