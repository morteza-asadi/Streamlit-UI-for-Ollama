from abc import ABC, abstractmethod
from typing import Dict, List

class ChatModel(ABC):
    @abstractmethod
    def stream_chat(self, messages: List[Dict[str, str]]) -> str:
        pass