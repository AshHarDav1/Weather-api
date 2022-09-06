import os
from dotenv import load_dotenv

# load_dotenv will look for a .env file and if it finds one
# it will load the environment variables from it
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


