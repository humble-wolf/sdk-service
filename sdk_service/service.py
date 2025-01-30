from sdk_service.client import HunterClient
from sdk_service.storage import Storage


class HunterService:

    def __init__(self) -> None:
        self.client = HunterClient()
        self.storage = Storage()

    def verify_email(self, email: str) -> dict:
        if cached := self.storage.get(email):
            return cached
        result = self.client.email_verifier(email)
        self.storage.save(email, result)
        return result
