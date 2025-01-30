import requests
from typing import Dict, Any
from sdk_service.config import HUNTER_API_KEY, HUNTER_BASE_URL


class HunterClient:

    def __init__(self) -> None:
        self.api_key: str = HUNTER_API_KEY
        self.base_url: str = HUNTER_BASE_URL

    def email_verifier(self, email: str) -> Dict[str, Any]:
        url = f"{self.base_url}/email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
