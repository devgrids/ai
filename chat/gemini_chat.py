from ai.chat.chat import Chat
from ai.ai_connection import AiType, AIConnection
import google.generativeai as genai

class GeminiChat(Chat):
    def __init__(self):
        super().__init__()
        AIConnection().configuration(AiType.GEMINI)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def send_message(self, message):
        response = self.chat.send_message(message)
        return response.text
    
    def get_history(self):
        return self.chat.history;
    
 