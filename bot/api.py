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
    print("HEADERS:", dict(r.headers))
    print("BODY:", r.text[:1000])   # أول 1000 حرف فقط

    try:
        return r.json()
    except Exception:
        return {
            "status": False,
            "error": "NOT_JSON",
            "body": r.text[:1000]
        }


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
