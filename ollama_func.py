import json
import requests

def llama_request_emotion(prompt, max_token=None):
    if prompt is None:
        return ""
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
    if prompt is None:
        return ""
    s = prompt.split()
    prompt = " ".join(s[:min(len(s), 25)])
    
    url = 'http://127.0.0.1:11434/api/chat'  # URL вашего сервера

    payload = {
        "model": "llama3.2:1b",
        "messages": [
            {
                "role": "system",
                "content": "Тебе нужно определять тип текста из списка: [Технологии/IT, Мероприятия, Знакомства, Творчество, Социальная активность, Новостные, Организации, Юмор, Образовательные, Здоровье, Торговля, 18+]"
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

def export_defined_theme(prompt):
    cgs = ["Технологии / IT", "Мероприятия", "Знакомства", "Творчество", "Социальная активность", "Новостные", "Организации", "Юмор", "Образовательные", "Здоровье", "Торговля", "18+"]
    for i in range(len(cgs)):
        if cgs[i] in prompt:
            return i + 1
    return 0

def export_defined_type(prompt):
    if "1" in prompt:
        return 1
    if "2" in prompt:
        return 2
    else:
        return 0