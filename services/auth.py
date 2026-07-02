from bot.config import USERNAME, PASSWORD
from services.api import post


def login():

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = post("User/signIn", payload)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    try:
        data = response.json()
        print("JSON:", data)
        return data.get("status", False)
    except Exception:
        print("NOT JSON RESPONSE")
        return False
