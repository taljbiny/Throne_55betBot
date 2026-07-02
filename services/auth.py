from bot.config import USERNAME, PASSWORD
from services.api import post


def login():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    try:
        response = post("User/signIn", payload)

        return {
            "status_code": response.status_code,
            "content_type": response.headers.get("content-type"),
            "text": response.text[:1000]
        }

    except Exception as e:
        return {
            "error": str(e)
        }
