import os
import pandas as pd
import json


class FileOperations:

    def open_file(file_name: str) -> str:
        try:
            with open(file_name, encoding='utf-8') as f:
                data = f.read()
                return data
        except:
            print("File not found: " + file_name)
            return False

    def load_classification_from_excel(file_name: str, sheetname: str) -> dict:
        try:
            loaded_data = pd.read_excel(file_name, sheetname, skiprows=5)
            result = loaded_data.to_dict()
            return result
        except:
            print("File not found: " + file_name)
            return False

    def load_subaccount_limitations_from_excel(file_name: str, sheetname: str) -> dict:
        try:
            loaded_data = pd.read_excel(file_name, sheetname)
            result = loaded_data.to_dict()
            return result
        except:
            print("File not found: " + file_name)
            return False

    def save_dict_to_json_file(dict_object: dict, file_name: str) -> bool:
        try:
            output = "JSON_files/export/" + file_name + ".json"
            with open(output, "w", encoding='utf-8') as outfile:
                json_object = json.dumps(dict_object, indent=4, ensure_ascii=False)  
                outfile.write(json_object)
                return True
        except:
            print("Saving data failed!")
            return False
