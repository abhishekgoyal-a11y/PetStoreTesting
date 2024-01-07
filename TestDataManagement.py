import os
import pandas as pd

class TestDataManagement:
    def __init__(self):
        print('Initialization of TestDataManagement class')

    def read_test_data(self, excel_file_name, sheet_name):
        return pd.read_excel(os.getcwd()+f'\\TestData\\{excel_file_name}.xlsx', sheet_name=sheet_name)