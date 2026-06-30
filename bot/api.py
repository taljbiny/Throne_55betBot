import requests

from bot.config import BASE_URL
from bot.config import USERNAME
from bot.config import PASSWORD


session = requests.Session()


def login():

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    r = session.post(
        f"{BASE_URL}/User/signIn",
        json=payload
    )

    data = r.json()

    return data["status"]
