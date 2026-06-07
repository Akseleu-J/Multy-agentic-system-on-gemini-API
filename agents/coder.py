from agents.base import GeminiAgent

class CoderAgent(GeminiAgent):
    def __init__(self, name: str):
        role = "Ты профессиональный разработчик, отвечаешь только с чистым кодом с комментариями"
        super().__init__(name, role=role, model="gemini-2.0-flash")