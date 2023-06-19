import openai

openai.api_key = "$OPENAI_API_KEY"

def narrate(text):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.5,
      max_tokens=100
    )

    return response.choices[0].text.strip()