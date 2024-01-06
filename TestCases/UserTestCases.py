from EndPoints.UserEndPoints import UserEndPoints

def create_user_test(url, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code):
    user = UserEndPoints(url)
    response = user.create_user(user_id, username, firstName, lastName, email, password, phone, userStatus)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def user_login_test(url, username, password, expected_status_code):
    user = UserEndPoints(url)
    response = user.user_login(username, password)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def get_user_test(url, username, expected_status_code):
    user = UserEndPoints(url)
    response = user.get_user(username)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def update_user_test(url, user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus, expected_status_code):
    user = UserEndPoints(url)
    response = user.update_user(user_id, username, newUsername, firstName, lastName, email, password, phone, userStatus)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def delete_user_test(url, username, expected_status_code):
    user = UserEndPoints(url)
    response = user.delete_user(username)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def user_logout_test(url, expected_status_code):
    user = UserEndPoints(url)
    response = user.user_logout()
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"