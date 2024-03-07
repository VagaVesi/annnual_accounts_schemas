from app.file_operations import FileOperations
from app.validator import Validator
from app.converter import Converter

def main():
    xml_document = FileOperations.open_file("XML_files/sample_reports/sample_report_micro.xml")
    # schema = FileOperations.open_file("files/validation_schemas/annual_accounts_micro.xsd")
    schema = "http://www.xbrl.org/taxonomy/int/gl/2015-03-25/plt/case-c-b-m/gl-plt-all-2015-03-25.xsd"
    # Validator.save_schema_locally(schema)

    validation_result = Validator.validate_xml(xml_document, schema)   
    if (validation_result == False):
        validation_result = Validator.get_xml_validation_errors(xml_document, schema)
    print("Finished:")
    print(validation_result)

    # if(validation_result == True):
    #     json = Converter.convert_xml_to_json(xml_document, schema)
    #     print(json)

if __name__ == "__main__":
    main()
