import json
import openai


with open('config.json', mode='r', encoding='utf-8') as file:
    openai.api_key = json.load(file)["api_key"]


def create_wish(name):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Сделай поздравление человеку с именем {name}. Добавь в него юмор",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
