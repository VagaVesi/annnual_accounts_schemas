import os
import pandas as pd  

class FileOperations:

    def open_file(file_name: str) -> str:
            try:
                with open(file_name, encoding='utf-8') as f:
                    data = f.read() 
                    return data
            except:
                 print("File not found: " + file_name)
                 return False
            
    def load_classification_from_excel(file_name: str, sheetname: str)-> dict:
       #loaded_data = pd.read_excel(file_name,sheetname, skiprows=4)
        try:
            loaded_data = pd.read_excel(file_name,sheetname, skiprows=5)
            result = loaded_data.to_dict()
            return result
        except:
                 print("File not found: " + file_name)
                 return False

                 