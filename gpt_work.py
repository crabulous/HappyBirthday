import json
import openai
import datetime
import requests
from date_work import season_and_sign

with open('config.json', mode='r', encoding='utf-8') as file:
    loaded = json.load(file)
    openai.api_key = loaded["gpt_api_key"]
    deep_key = loaded["deep_api_key"]


def create_wish(name):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Сделай поздравление с днём рождения человеку с именем {name}. Добавь в него юмор",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


# def create_image():
#     response = openai.Image.create(
#         prompt=f"Открытка на день рождения без текста",
#         n=2,
#         size="1024x1024"
#     )
#     image_url = response['data'][0]['url']
#     return image_url


def deepai():
    now = datetime.datetime.now()
    month_now = now.month
    day_now = now.day
    res = season_and_sign(month_now, day_now)
    season = res[0]
    sign = res[1]
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': f'{season} Holiday in fantasy style with a beautiful landscape background, without text on photo, make it about {sign}.',
            'grid_size': '1',
        },
        headers={'api-key': deep_key}
    )
    return r.json()["output_url"]