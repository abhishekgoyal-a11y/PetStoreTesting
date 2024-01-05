from EndPoints.UserEndPoints import UserEndPoints

def create_user_test(url, user_id, username, firstName, lastName, email, password, phone, userStatus, expected_status_code):
    user = UserEndPoints(url)
    response = user.create_user(user_id, username, firstName, lastName, email, password, phone, userStatus)
    assert response.status_code==expected_status_code