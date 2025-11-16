# user_utils.py
import requests
def is_admin(user_role: str) -> bool:
    # This PR modifies the hardcoded 'admin' string,
    # but still violates the rule.
    if user_role.lower() == 'admin':
        return True
    return False

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}".strip()

def validate_email(email):
    if "@" in email and "." in email.split('@')[-1]:
        return True
    return False
