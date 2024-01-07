from EndPoints.StoreEndPoints import StoreEndPoints

def create_order_test(url, order_id, pet_id, quantity, shipDate, status, complete, expected_status_code):
    store = StoreEndPoints(url)
    if complete in [1.0, 1]:
        complete = True
    elif complete in [0.0, 0]:
        complete = False
    response = store.create_order(order_id, pet_id, quantity, shipDate, status, complete)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def get_order_test(url, order_id, expected_status_code):
    store = StoreEndPoints(url)
    response = store.get_order(order_id)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def get_inventory_test(url, expected_status_code):
    store = StoreEndPoints(url)
    response = store.get_inventory()
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"

def delete_order_test(url, order_id, expected_status_code):
    store = StoreEndPoints(url)
    response = store.delete_order(order_id)
    assert response.status_code==expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}. Error message: {response.text}"
