import openai


class OpenAI:
    def __init__(self):
        pass

    def ask_ChatGPT(self, query):
        openai.api_key = "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"

        request = {"role": "user", "content": query}

        res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[request], temperature=1, max_tokens=128, top_p=1, frequency_penalty=0, presence_penalty=0)

        print(res.choices[0]["message"]["content"])

        response = res.choices[0]["message"]["content"]

        sentence_end = [".", "!", "?"]
        for end in reversed(response):
            if end in sentence_end:
                response = response[: response.rindex(end) + 1]
                break

        print(response)
