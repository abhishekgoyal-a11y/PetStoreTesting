import pandas as pd

class TestDataManagement:
    def __init__(self):
        print('Initialization of TestDataManagement class')

    def read_test_data(self, sheet_name):
        return pd.read_excel(r'C:\Users\abgoyal\Downloads\PetStoreTesting\TestData\Users.xlsx', sheet_name=sheet_name)