import json
import requests

def llama_request_emotion(prompt, max_token=None):
    s = prompt.split()
    prompt = " ".join(s[:min(len(s), 25)])

    url = 'http://127.0.0.1:11434/api/chat' # URL вашего сервера

    payload = {
        "model": "llama3.2:1b",
        "messages": [
            {
                "role": "system",
                "content": "Тебе нужно написать 0, если текст неэмоциональный, 1 - если эмоциональный, 2 - если негативный:"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "options": {
          "temperature": 0.1,
        },
        "stream": False,
        "max_token": max_token
    }

    # Отправка POST-запроса
    response = requests.post(
        url,
        data=json.dumps(payload)
    )
    return response.json()['message']['content']


def llama_request_theme(prompt, max_token=None):
    s = prompt.split()
    prompt = " ".join(s[:min(len(s), 25)])

    url = 'http://127.0.0.1:11434/api/chat'  # URL вашего сервера

    payload = {
        "model": "llama3.2:1b",
        "messages": [
            {
                "role": "system",
                "content": "Тебе нужно написать 0, если текст неэмоциональный, 1 - если эмоциональный, 2 - если негативный:"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "options": {
            "temperature": 0.1,
        },
        "stream": False,
        "max_token": max_token
    }

    # Отправка POST-запроса
    response = requests.post(
        url,
        data=json.dumps(payload)
    )
    return response.json()['message']['content']