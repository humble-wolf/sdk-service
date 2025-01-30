from sdk_service.client import HunterClient

client = HunterClient()


email = "test@email.com"

print(client.email_verifier(email))