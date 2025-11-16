# api_client.py
import requests
import logging

BASE_URL = "https://api.example.com/v1"

def get_user_data(user_id: int) -> dict:
    try:
        # This request is missing a timeout!
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        response.raise_for_status() # Good, this was added
        return response.json()
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error for user {user_id}: {e}")
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": "API request failed"}

def get_post_data(post_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
    return response.json()
