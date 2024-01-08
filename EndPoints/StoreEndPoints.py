import json
from API import API

class StoreEndPoints:

    def __init__(self, url):
        print('Initialization of StoreEndPoints class')
        self.store_url = f'{url}store'

    def create_order(self, order_id, pet_id, quantity, shipDate, status, complete):
        url = self.store_url + '/order'
        payload = {
                "id": order_id,
                "petId": pet_id,
                "quantity": quantity,
                "shipDate": shipDate,
                "status": status,
                "complete": complete
        }
        payload = json.dumps(payload)
        response = API.get_instance().post_request(url, payload)
        return response

    def delete_order(self, order_id):
        url = self.store_url + f'/order/{order_id}'
        payload = {}
        response = API.get_instance().delete_request(url, payload)
        return response

    def get_order(self, order_id):
        url = self.store_url + f'/order/{order_id}'
        payload = {}
        response = API.get_instance().get_request(url, payload)
        return response

    def get_inventory(self):
        url = self.store_url + '/inventory'
        payload = {}
        response = API.get_instance().get_request(url, payload)
        return response