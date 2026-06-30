import requests

from bot.config import BASE_URL, USERNAME, PASSWORD

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://agents.55bets.net/",
    "Origin": "https://agents.55bets.net",
    "Accept": "application/json, text/plain, */*"
})


def login():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    try:
        r = session.post(
            f"{BASE_URL}/User/signIn",
            json=payload,
            timeout=30
        )

        print("=" * 60)
        print("LOGIN STATUS:", r.status_code)
        print("LOGIN URL:", r.url)
        print("LOGIN HEADERS:", dict(r.headers))
        print("LOGIN BODY:")
        print(r.text[:1000])
        print("=" * 60)

        try:
            return r.json()
        except Exception:
            return {
                "status": False,
                "message": "Server did not return JSON",
                "body": r.text[:500]
            }

    except Exception as e:
        print("LOGIN ERROR:", str(e))
        return {
            "status": False,
            "message": str(e)
        }


def get_players():

    payload = {
        "start": 0,
        "limit": 10,
        "filter": {}
    }

    try:
        r = session.post(
            f"{BASE_URL}/Statistics/getPlayersStatisticsPro",
            json=payload,
            timeout=30
        )

        print("=" * 60)
        print("PLAYERS STATUS:", r.status_code)
        print("PLAYERS BODY:")
        print(r.text[:1000])
        print("=" * 60)

        try:
            return r.json()
        except Exception:
            return {
                "status": False,
                "message": "Server did not return JSON",
                "body": r.text[:500]
            }

    except Exception as e:
        print("PLAYERS ERROR:", str(e))
        return {
            "status": False,
            "message": str(e)
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

    try:
        r = session.post(
            f"{BASE_URL}/Player/registerPlayer",
            json=payload,
            timeout=30
        )

        print("=" * 60)
        print("CREATE STATUS:", r.status_code)
        print("CREATE BODY:")
        print(r.text[:1000])
        print("=" * 60)

        try:
            return r.json()
        except Exception:
            return {
                "status": False,
                "message": "Server did not return JSON",
                "body": r.text[:500]
            }

    except Exception as e:
        print("CREATE ERROR:", str(e))
        return {
            "status": False,
            "message": str(e)
        }
