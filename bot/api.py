import requests

from bot.config import BASE_URL, USERNAME, PASSWORD

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://agents.55bets.net/",
    "Origin": "https://agents.55bets.net"
})


def login():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    r = session.post(
        f"{BASE_URL}/User/signIn",
        json=payload
    )

    print("STATUS:", r.status_code)
    print("TEXT:", r.text)

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
