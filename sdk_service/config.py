import os
from dotenv import load_dotenv
load_dotenv(override=True)

print(os.getenv("HUNTER_API_KEY"))