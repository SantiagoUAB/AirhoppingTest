import requests

class Cars:

    def __init__(self):
        pass

    @staticmethod
    def download_seat_leon_specifications():
        r = requests.get('http://localhost/dummy_url')
        if r.status_code == 200:
            return r.json()
        return None