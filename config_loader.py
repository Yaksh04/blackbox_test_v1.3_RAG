# config_loader.py
import json
import sys

def load_config(config_path: str) -> dict:
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}", file=sys.stderr)
        sys.exit(1)

def get_setting(config: dict, key: str, default=None):
    return config.get(key, default)
