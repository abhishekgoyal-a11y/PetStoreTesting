import os
import pytest
from Config import DefaultsConfig
from TestCases.PetTestCases import *
from TestCases.StoreTestCases import *
from TestCases.UserTestCases import *
from TestDataManagement import TestDataManagement

def setup_module():
    global url
    defaults_config = DefaultsConfig.get_instance()
    defaults_config.read_yaml_file(os.getcwd()+'\\Config.yaml')
    url = defaults_config.get_config_value("url")

@pytest.mark.parametrize("action, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code",
                         TestDataManagement().read_test_data("Users", "Users").values)
def test_execute_users(action, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code):

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

@pytest.mark.parametrize("action, order_id, pet_id, quantity, shipDate, status, complete, expected_status_code",
                         TestDataManagement().read_test_data("Stores", "Stores").values)
def test_execute_users(action, order_id, pet_id, quantity, shipDate, status, complete, expected_status_code):
    if action == "create_order_test":
        create_order_test(url, order_id, pet_id, quantity, shipDate, status, complete, expected_status_code)
    elif action == "get_order_test":
        get_order_test(url, order_id, expected_status_code)
    elif action == "delete_order_test":
        delete_order_test(url, order_id, expected_status_code)
    elif action == "get_inventory_test":
        get_inventory_test(url, expected_status_code)

@pytest.mark.parametrize("action, payload, expected_status_code",
                         TestDataManagement().read_test_data("Pets", "Pets").values)
def test_execute_users(action, payload, expected_status_code):
    if action == "create_pet_test":
        create_pet_test(url, payload, expected_status_code)
