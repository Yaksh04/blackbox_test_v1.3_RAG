# api_client.py
import requests
import logging

BASE_URL = "https://api.example.com/v1"

def get_user_data(user_id: int) -> dict:
    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e: # This is a broad exception!
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": "An unknown error occurred"}

def get_post_data(post_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
    return response.json()
