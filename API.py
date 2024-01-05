import logging
import requests


class API:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if API.__instance is None:
            API.__instance = API()

        return API.__instance

    def __init__(self):
        print('Initialization of API class')
        if API.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            API.__instance = self

        self.logger = logging.getLogger()

    def post_request(self, url, payload, content_type=None):
        if content_type is None:
            content_type = 'application/json'
        headers = {
            'Content-Type': content_type
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        self.logger.info('response_status_code: %s response_text: %s', response.status_code, response.text)
        return response

    def get_request(self, url, payload, content_type=None):
        if content_type is None:
            content_type = 'application/json'
        headers = {
            'Content-Type': content_type
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        self.logger.info('response_text: %s', response.text)
        return response

    def put_request(self, url, payload, content_type=None):
        if content_type is None:
            content_type = 'application/json'
        headers = {
            'Content-Type': content_type
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.logger.info('response_text: %s', response.text)
        return response

    def patch_request(self, url, payload, content_type=None):
        if content_type is None:
            content_type = 'application/json'
        headers = {
            'Content-Type': content_type
        }
        response = requests.request('PATCH', url, headers=headers, data=payload)
        self.logger.info('response_text: %s', response.text)
        return response

    def delete_request(self, url, payload, content_type=None):
        if content_type is None:
            content_type = 'application/json'
        headers = {
            'Content-Type': content_type
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.logger.info('response_text: %s', response.text)
        return response