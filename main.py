from EndPoints.UserEndPoints import UserEndPoints

user = UserEndPoints("https://petstore.swagger.io/v2/")
user.create_user(
    2,
                 'username', 'firstName', 'lastName', 'email', 'password',
                 'phone', 1)