import json
import os

DATA_DIR = "data"

def ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_json(filename, default):
    ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        save_json(filename, default)
        return default
    with open(path, "r") as f:
        return json.load(f)

def save_json(filename, data):
    ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
