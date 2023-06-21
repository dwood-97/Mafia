import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def narrate(text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text,
        temperature=0.5,
        max_tokens=100,
        n = 1,
        stop = None,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
    return response.choices[0].text.strip()
