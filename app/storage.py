#  Simple persistence layer to save and load issue data to/from a JSON file instead of using a database.
from pathlib import Path
import json

DATA_DIR = Path('data')
DATA_FILES = DATA_DIR / 'issues.json'

def load_data():
    if DATA_FILES.exists():
        with open(DATA_FILES, "r") as f:
            content = f.read()
            if content.strip(): # Checks if file is not empty (ignores whitespace)
                return json.loads(content) #return json.loads(content) - Parses JSON string and returns as Python list/dict
    return []

def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILES, "w") as f:
        json.dump(data, f, indent=2)