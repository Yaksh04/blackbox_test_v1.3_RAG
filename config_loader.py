# config_loader.py
# Responsible for loading application configuration.

import json

def load_config(config_path: str) -> dict:
    """
    Loads a JSON configuration file.
    
    NOTE: Does not handle FileNotFoundError.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def get_setting(config: dict, key: str, default=None):
    """
    Retrieves a specific setting from the config dict.
    
    NOTE: This is a simple wrapper.
    """
    return config.get(key, default)