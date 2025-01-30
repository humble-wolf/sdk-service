from sdk_service.client import HunterClient
from sdk_service.storage import Storage


class HunterService:

    def __init__(self) -> None:
        self.client = HunterClient()
        self.storage = Storage()

    def verify_email(self, email: str) -> dict:
        cached_response = self.storage.get(email)
        if cached_response is not None:
            return cached_response

        email_verification_data = self.client.email_verifier(email)
        self.storage.save(email, email_verification_data)

        return email_verification_data
