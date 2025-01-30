import unittest
from unittest.mock import patch
from sdk_service.service import HunterService


class TestHunterService(unittest.TestCase):

    @patch("sdk_service.service.HunterClient.email_verifier")
    def test_verify_email(self, mock_email_verifier):
        mock_email_verifier.return_value = {
            "data": {
                "email": "test@example.com",
                "status": "valid",
            }
        }

        service = HunterService()
        result = service.verify_email("test@example.com")

        self.assertEqual(result["data"]["email"], "test@example.com")


if __name__ == "__main__":
    unittest.main()
