import xmlschema;
import jsonschema;
from app.file_operations import FileOperations
import json

class Validator:
    """Validates files against schemas"""

    def validate_xml(xml_document: str, schema: str) -> bool :
        if(xml_document == False or schema == False):
            return False
        return xmlschema.is_valid(xml_document, schema)
       
    def get_xml_validation_errors(xml_document: str, schema: str) -> str:
        if(xml_document == False or schema == False):
            return False
        return xmlschema.validate(xml_document,  schema)
    
    def save_schema_locally(xsd_full_path: str) -> bool:
        try:
            schema = xmlschema.XMLSchema(xsd_full_path)
            schema.export(target='XML_files/validation_schemas/download', save_remote=True)
            print("file saved")
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def validate_json(json_document: str, schema: str) -> bool:
        source_instance = FileOperations.open_file(json_document)
        source_xs = FileOperations.open_file(schema)
        instance = json.loads(source_instance)
        xs = json.loads(source_xs)
        return jsonschema.validate(instance=instance, schema=xs)