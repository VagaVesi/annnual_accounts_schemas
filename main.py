from app.validator import Validator
from app.file_operations import FileOperations
from app.converter import Converter
from app.xbrlgl_validator import XBRLGLValidator

def main():
    # json_document = "JSON_files/samples/classification_varagrupp.json"
    # json_schema = "JSON_files/schemas/classification_elements_schema.json"
    # xls_file = "JSON_files/import/AA_MAJANDUSTEHINGUD_20231102.xlsx"

    # classification_code = "ANDMETEESITLUSVIIS2024ap"

    # raw_data = FileOperations.load_classification_from_excel(xls_file, classification_code)

    # #print(raw_data)

    # result = Converter.convert_xls_to_classification_json(raw_data, classification_code)

    # json_document = "JSON_files/samples/test_if_valid.json"
    # json_schema = "JSON_files/schemas/test_if_schema.json"

    # validation_result = Validator.validate_json(json_document, json_schema)
    # print(validation_result)

    xlm_file = FileOperations.open_file("XML_files/sample_reports/EE0301020_sample_report_stardard_small.xml")
    is_xml_valid = Validator.validate_xml(xlm_file, "http://www.xbrl.org/taxonomy/int/gl/2015-03-25/plt/case-c-b-m/gl-plt-all-2015-03-25.xsd")
    print ("validation result: ", is_xml_valid)

    data_from_xml_file = Converter.convert_xml_to_dict('XML_files/sample_reports/EE0301020_sample_report_stardard_small.xml')
    clean = XBRLGLValidator.format_xbrlgl_to_dict(data_from_xml_file)
    is_equal = XBRLGLValidator.compare_debit_credit(clean)
    print(is_equal)



if __name__ == "__main__":
    main()
