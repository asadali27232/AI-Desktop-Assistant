# import openai

# openai.api_key = "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"

# request = {"role": "user", "content": "Hello, how are you?"}

# response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[request], temperature=1, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)

# print(response.choices[0]["message"]["content"])

# import os

# os.system("calc.exe")

class MyClass:
    def calculate_sum(self, a, b):
        return a + b

# Create an instance of the class
my_object = MyClass()

# Call the class method and store the returned value
result = my_object.calculate_sum(3, 5)

# Print the returned value
print(result)