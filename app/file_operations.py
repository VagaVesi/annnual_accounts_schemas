import pandas as pd
import json


class FileOperations:
    """Load data from file or save data to file."""

    def open_file(file_name: str) -> str:
        try:
            with open(file_name, encoding='utf-8') as f:
                data = f.read()
                return data
        except:
            print("File not found: " + file_name)
            return False

    def load_data_from_excel_return_dict(file_name: str, sheetname: str, skip_rows: int) -> dict:
        """Load data from excel file."""
        try:
            loaded_data = pd.read_excel(file_name, sheetname, skiprows=skip_rows)
            result = loaded_data.to_dict()
            return result
        except:
            print("File not found: " + file_name)
            return False


    def save_dict_to_json_file(dict_object: dict, file_name: str) -> bool:
        """Make json file from dict"""
        try:
            output = "JSON_files/export/" + file_name + ".json"
            with open(output, "w", encoding='utf-8') as outfile:
                json_object = json.dumps(dict_object, indent=4, ensure_ascii=False)  
                outfile.write(json_object)
                return True
        except:
            print("Saving data failed!")
            return False
