import os
import pytest
from Config import DefaultsConfig
from TestCases.UserTestCases import create_user_test
from TestDataManagement import TestDataManagement

def setup_module():
    global url
    defaults_config = DefaultsConfig.get_instance()
    defaults_config.read_yaml_file(os.getcwd()+'\\Config.yaml')
    url = defaults_config.get_config_value("url")

@pytest.mark.parametrize("action, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code",
                         TestDataManagement().read_test_data("Users").values)
def test_execute(action, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code):
    if action == "create_user_test":
        create_user_test(url, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code)
