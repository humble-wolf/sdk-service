from sdk_service.service import HunterService

service = HunterService()

email = "test@example.com"
print("Verifying email:", service.verify_email(email))
