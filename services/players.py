from services.api import post


def get_players(start=0, limit=10):

    payload = {
        "start": start,
        "limit": limit,
        "filter": {}
    }

    response = post(
        "Statistics/getPlayersStatisticsPro",
        payload
    )

    try:
        return response.json()
    except Exception:
        return None
