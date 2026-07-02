from bot.config import USERNAME, PASSWORD
from services.api import post


def login():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = post("User/signIn", payload)

    print("=" * 50)
    print("STATUS:", response.status_code)
    print("HEADERS:", response.headers.get("content-type"))
    print("TEXT:", response.text)
    print("=" * 50)

    try:
        data = response.json()
        return data.get("status", False)
    except Exception:
        return False
