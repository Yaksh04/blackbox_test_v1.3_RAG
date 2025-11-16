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

def format_user_for_display(user_obj):
    # This function is missing type hints!
    name = get_full_name(user_obj.first, user_obj.last)
    return f"{name} ({user_obj.email})"
