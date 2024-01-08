from EndPoints.PetEndPoints import PetEndPoints

def create_pet_test(url, payload, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.create_pet(payload)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def create_pet_by_id_test(url, pet_id, name, status, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.create_pet_by_id(pet_id, name, status)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def update_pet_test(url, payload, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.update_pet(payload)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def get_pet_test(url, pet_id, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.get_pet(pet_id)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def get_pet_by_status_test(url, pet_status, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.get_pet_by_status(pet_status)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def delete_pet_test(url, pet_id, expected_status_code):
    pet = PetEndPoints(url)
    response = pet.delete_pet(pet_id)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"