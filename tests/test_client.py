import unittest
from unittest.mock import patch
from sdk_service.client import HunterClient


class TestHunterClient(unittest.TestCase):

    @patch("sdk_service.client.requests.get")
    def test_email_verifier(self, mock_get):
        mock_get.return_value.json.return_value = {"data": {"email": "test@example.com", "status": "valid"}}
        mock_get.return_value.raise_for_status = lambda: None
        
        client = HunterClient()
        result = client.email_verifier("test@example.com")
        self.assertEqual(result["data"]["email"], "test@example.com")


if __name__ == "__main__":
    unittest.main()
