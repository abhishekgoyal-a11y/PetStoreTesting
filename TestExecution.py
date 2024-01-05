import pytest
from TestCases.UserTestCases import create_user_test
from Tests.TestDataManagement import TestDataManagement

@pytest.mark.parametrize("action, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code",
                         TestDataManagement().read_test_data("Users").values)
def test_execute(action, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code):
    if action == "create_user_test":
        create_user_test("https://petstore.swagger.io/v2/", user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code)
