import requests

class ImportAPI:
    def __init__(self, base_url, token):
        self.url = f"{base_url}/import"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def post_person(self, person_id):
        body = [{"personId": person_id}]
        try:
            response = requests.post(self.url, headers=self.headers, json=body)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None