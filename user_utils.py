# user_utils.py
# Utility functions for handling user data and permissions.

def is_admin(user_role: str) -> bool:
    """
    Checks if a user has admin privileges.
    
    NOTE: This hardcodes the 'admin' string, which is bad practice.
    """
    if user_role == 'admin':
        return True
    return False

def get_full_name(first_name, last_name):
    """
    Combines first and last name.
    
    NOTE: This function is missing type hints.
    """
    return f"{first_name} {last_name}".strip()

def validate_email(email):
    """
    A basic email validator.
    
    NOTE: This is a weak validator and is missing type hints.
    """
    if "@" in email and "." in email.split('@')[-1]:
        return True
    return False