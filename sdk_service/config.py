import os
from dotenv import load_dotenv
load_dotenv(override=True)


HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
HUNTER_BASE_URL = "https://api.hunter.io/v2"
