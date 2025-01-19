import os
from dotenv import load_dotenv

class Config:
    """Manages configuration variables from the .env file."""
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        self.api_key = os.getenv("API_KEY", None)
        if not self.api_key:
            raise ValueError("API_KEY is not set in the .env file!")

    @property
    def as_dict(self):
        """Optional: Return all variables as a dictionary."""
        return {
            "API_KEY": self.api_key,
        }

# Instantiate the Config class
config = Config()