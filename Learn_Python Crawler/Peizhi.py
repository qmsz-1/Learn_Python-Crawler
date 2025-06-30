import json

config = {
    "debug": True,
    "log_level": "INFO",
    "max_retries": 3,
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret"
    }
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)