# user_utils.py
import requests
def is_admin(user_role: str) -> bool:
    if user_role == 'admin':
        return True
    return False

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}".strip()

def validate_email(email):
    if "@" in email and "." in email.split('@')[-1]:
        return True
    return False

def get_initials(first_name: str, last_name: str):
    # This function is missing a docstring!
    return f"{first_name[0]}{last_name[0]}"
