from bot.config import USERNAME, PASSWORD
from services.api import post


def login():

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = post(
        "User/signIn",
        payload
    )

    try:
        data = response.json()
    except Exception:
        return False

    return data.get("status", False)
