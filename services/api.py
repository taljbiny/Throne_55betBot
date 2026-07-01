import requests
from bot.config import BASE_URL

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://agents.55bets.net",
    "Referer": "https://agents.55bets.net/",
    "X-Requested-With": "XMLHttpRequest",
})


def post(endpoint, payload):
    response = session.post(
        f"{BASE_URL}/{endpoint}",
        json=payload,
        timeout=30
    )

    return response
