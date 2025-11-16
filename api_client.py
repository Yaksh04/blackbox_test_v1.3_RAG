# api_client.py
# A simple client for fetching data from an external service.

import requests
import logging

# Configuration (ideally from env)
BASE_URL = "https://api.example.com/v1"

def get_user_data(user_id: int) -> dict:
    """
    Fetches user data from the API.
    
    WARNING: Lacks proper error handling and timeouts.
    """
    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        # Missing check for response.status_code
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": "API request failed"}

def get_post_data(post_id: int) -> dict:
    """Fetches post data."""
    # This function is missing type hints and has a hardcoded timeout
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
    return response.json()