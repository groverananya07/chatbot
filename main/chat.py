import anthropic

class ChatBot:
    def __init__(self, api_key, model="claude-3-opus-20240229", max_tokens=1000, temperature=0.0):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.max_tokens = max_tokens
        self.model = model
        self.temperature = temperature

    def chat(self, system_content, user_content):
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_content,
            messages=[
                {"role": "user", "content": user_content}
            ]
        )
        return message.content[0].text

