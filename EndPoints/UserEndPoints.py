import json
from API import API
import logging

class UserEndPoints:

    def __init__(self, url):
        print('Initialization of UserEndPoints class')
        self.user_url = f'{url}user'
        self.logger = logging.getLogger()

    def create_user(self, user_id, username, firstName, lastName, email, password, phone, userStatus):
        payload = {
              "id": user_id,
              "username": username,
              "firstName": firstName,
              "lastName": lastName,
              "email": email,
              "password": password,
              "phone": phone,
              "userStatus": userStatus
            }
        payload = json.dumps(payload)
        self.logger.info('Payload: %s URL: %s', payload, self.user_url)
        response = API.get_instance().post_request(self.user_url, payload)
        return response

    def create_with_list(self, payload):
        url = self.user_url+'createWithList'
        payload = json.dumps(payload)
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().post_request(url, payload)
        return response

    def create_with_array(self, payload):
        url = self.user_url+'createWithArray'
        payload = json.dumps(payload)
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().post_request(url, payload)
        return response

    def user_logout(self):
        payload = {}
        url = self.user_url+'/logout'
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().get_request(url, payload)
        return response

    def user_login(self, username, password):
        url = self.user_url+f'/login?username={username}&password={password}'
        payload = {}
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().get_request(url, payload)
        return response

    def delete_user(self, username):
        url = self.user_url+f'/{username}'
        payload = {}
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().delete_request(url, payload)
        return response

    def get_user(self, username):
        url = self.user_url+f'/{username}'
        payload = {}
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().get_request(url, payload)
        return response

    def update_user(self, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus):
        url = self.user_url+f'/{username}'
        payload = {
              "id": user_id,
              "username": newUsername,
              "firstName": firstName,
              "lastName": lastName,
              "email": email,
              "password": password,
              "phone": phone,
              "userStatus": userStatus
            }
        payload = json.dumps(payload)
        self.logger.info('Payload: %s URL: %s', payload, url)
        response = API.get_instance().put_request(url, payload)
        return response