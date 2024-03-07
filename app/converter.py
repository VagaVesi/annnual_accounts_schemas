import xmlschema;
from pandas import notna
import xmltodict
from app.file_operations import FileOperations

class Converter:

    def convert_xml_to_json(xml_document:str, schema: str) -> dict:
        xs = xmlschema.XMLSchema(schema)
        result = xs.to_dict(xml_document)
        return result
    
    def convert_xml_to_dict(xml_document_path:str) -> dict:
        loaded_data = FileOperations.open_file(xml_document_path)
        result = xmltodict.parse(loaded_data, xml_attribs=False)
        return result
    
    def convert_xls_to_classification_json(xls_raw: dict, classification_code: str) -> dict:
        result = {"classification_code": classification_code,
                  "elements":[]}
        elements_count = len(xls_raw['code'])
        for i in range(0, elements_count):  
            element = {'code': '','name':{},'explanation':{}, 'selectable':0, "level":1}
            for x, y in xls_raw.items():
                if notna(y[i]):
                    if x == 'name_ET':
                        element['name'].update({'et': y[i]})
                    elif x == 'name_EN':
                        element['name'].update({'en': y[i]})
                    elif x == 'explanation_ET':
                        element['explanation'].update({'et': y[i]})
                    elif x == 'explanation_EN':
                        element['explanation'].update({'en': y[i]})
                    elif x == 'validFromDate':
                        element['valid_from_date'] = str(y[i].date())[:10]
                    elif x == 'parentCode':
                        element['parent_code'] = y[i]   
                    else:
                        element[x] = y[i]
            result["elements"].append(element)
        return result
    

