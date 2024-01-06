import os
import pytest
from Config import DefaultsConfig
from TestCases.UserTestCases import *
from TestDataManagement import TestDataManagement

def setup_module():
    global url
    defaults_config = DefaultsConfig.get_instance()
    defaults_config.read_yaml_file(os.getcwd()+'\\Config.yaml')
    url = defaults_config.get_config_value("url")

@pytest.mark.parametrize("action, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code",
                         TestDataManagement().read_test_data("Users").values)
def test_execute(action, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code):

    if action == "create_user_test":
        create_user_test(url, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code)
    elif action == "user_login_test":
        user_login_test(url, username, password, expected_status_code)
    elif action == "get_user_test":
        get_user_test(url, username, expected_status_code)
    elif action == "delete_user_test":
        delete_user_test(url, username, expected_status_code)
    elif action == "update_user_test":
        update_user_test(url, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code)
