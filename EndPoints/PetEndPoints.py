import json
from API import API

class PetEndPoints:
    def __init__(self, url):
        print('Initialization of PetEndPoints class')
        self.pet_url = f'{url}pet'

    def create_pet(self, payload):
        response = API.get_instance().post_request(self.pet_url, payload)
        return response

    def create_pet_by_id(self, pet_id, name, status):
        url = self.pet_url+f'/{pet_id}'
        payload = {
                "name": name,
                "status": status
        }
        payload = json.dumps(payload)
        response = API.get_instance().post_request(url, payload)
        return response

    def update_pet(self, payload):
        response = API.get_instance().put_request(self.pet_url, payload)
        return response

    def get_pet(self, pet_id):
        url = self.pet_url+f'/{pet_id}'
        payload = {}
        response = API.get_instance().get_request(url, payload)
        return response

    def get_pet_by_status(self, pet_status):
        url = self.pet_url+f'/findByStatus?status={pet_status}'
        payload = {}
        response = API.get_instance().get_request(url, payload)
        return response

    def delete_pet(self, pet_id):
        url = self.pet_url+f'/{pet_id}'
        payload = {}
        response = API.get_instance().delete_request(url, payload)
        return response
