import openai


class OpenAI:
    def __init__(self):
        pass

    def ask_ChatGPT(self, query, words=100):
        openai.api_key = "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"

        request = {"role": "user", "content": query}

        res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[request], temperature=1, max_tokens=words, top_p=1, frequency_penalty=0, presence_penalty=0)

        response = res.choices[0]["message"]["content"]

        # Get the first peragraph only to speak and avoid speaking the whole long text
        return response
