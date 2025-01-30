import requests
from sdk_service.config import HUNTER_API_KEY, HUNTER_BASE_URL


class HunterClient:

    def __init__(self) -> None:
        self.api_key = HUNTER_API_KEY
        self.base_url = HUNTER_BASE_URL

    def email_verifier(self, email: str) -> dict:
        url = f"{self.base_url}/email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
