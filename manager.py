import json
import os
FILE = "data.json"
def load_json():
        if os.path.exists(FILE):
            with open(FILE, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        return data

def save(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_code(code):
    data = load_json()
    data[code] = code
    save(data)
