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

    return r.json()


def get_players():

    payload = {
        "start": 0,
        "limit": 10,
        "filter": {}
    }

    r = session.post(
        f"{BASE_URL}/Statistics/getPlayersStatisticsPro",
        json=payload
    )

    return r.json()


def create_player(login_name, password):

    payload = {
        "player": {
            "email": f"{login_name}@player.nsp",
            "password": password,
            "parentId": "2598761",
            "login": login_name
        }
    }

    r = session.post(
        f"{BASE_URL}/Player/registerPlayer",
        json=payload
    )

    return r.json()
