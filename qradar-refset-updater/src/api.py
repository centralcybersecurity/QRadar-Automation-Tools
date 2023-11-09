import requests

BASE_URL = "https://qradar.example.com"
AUTH_TOKEN = "xxx"

def get_ref_set(name):
  url = f"{BASE_URL}/api/reference_data/sets/{name}"

  headers = {"SEC": AUTH_TOKEN}

  response = requests.get(url, headers=headers)
  return response.json()

def update_ref_set(name, data):
  url = f"{BASE_URL}/api/reference_data/sets/{name}"

  headers = {"SEC": AUTH_TOKEN}

  response = requests.post(url, headers=headers, json=data)
  return response.status_code