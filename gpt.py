from openai import OpenAI
import os

class MODEL():

    def __init__(self):
        self.client = OpenAI(api_key = '')

    def get_response(self,user_prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            temperature=0.7,
            max_tokens=50,
            messages=[
                {
            "role": "system",
            "content": (
            "You are an expert in English grammar and style. "
            "Your task is to correct and improve the following sentence for grammar, clarity, and style. "
            "Make sure the sentence is free of typos, grammatical errors, and is well-structured. "
            "Here is the sentence to improve:\n\n"
            f"{user_prompt}"
                )
            }
        ]
    )
        return response.choices[0].message.content