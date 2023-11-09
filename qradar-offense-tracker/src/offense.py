import requests
from config import HOST, TOKEN 

class Offense:

    def __init__(self, id, status):
        self.id = id
        self.status = status

    def update_status(self, new_status):
        url = f'{HOST}/api/siem/offenses/{self.id}'
        headers = {'SEC': TOKEN}
        data = {'status': new_status}

        response = requests.patch(url, headers=headers, json=data)
        if response.ok:
            self.status = new_status
            print(f'Offense {self.id} status updated to {new_status}')
        else:
            print(f'Error updating offense {self.id}: {response.text}')