from typing import List, Dict
import streamlit as st

class ChatHistory:
    def __init__(self):
        if 'messages' not in st.session_state:
            st.session_state.messages = []

    def add_message(self, role: str, content: str):
        st.session_state.messages.append({"role": role, "content": content})

    def clear_history(self):
        st.session_state.messages = []

    def get_messages(self) -> List[Dict[str, str]]:
        return st.session_state.messages