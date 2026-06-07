from agents.base import GeminiAgent

class TesterAgent(GeminiAgent):
    def __init__(self, name: str):
        role = "Ты профессиональный тестировщик, пишешь тесты для предоставленного кода"
        super().__init__(name, role=role, model="gemini-2.0-flash")