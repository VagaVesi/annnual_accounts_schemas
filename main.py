from app.validator import Validator
from app.file_operations import FileOperations
from app.converter import Converter
from app.xbrlgl_validator import XBRLGLValidator
from datetime import datetime


def main():
    """Make classification JSON file."""
    # xls_file = "JSON_files/import/AA_MAJANDUSTEHINGUD_2024-03-19.xlsx"
    # classification_code = "ANDMETEESITLUSVIIS2024ap"
    # classification_name_ML = {"et": "Deebet või kreedit muutuse liik", "en":"Type of debit or credit change"}
    # classification_name_VG = {"et": "Vara grupp", "en":"Asset group"}
    # classification_name_SOP = {"et": "Seotud osapoole liik", "en":"Type of related party"}
    # classification_name = {"et": "Andmete esitlusviis", "en":"Presentation of data"}
    # raw_data = FileOperations.load_classification_from_excel(xls_file, classification_code)
    # result = Converter.convert_xls_to_classification_json(raw_data, classification_code, classification_name)
    # FileOperations.save_dict_to_json_file(result, classification_code)

    """Validate JSON sample."""
    json_document = "JSON_files/sample_reports/standard_error_bussiness_debit_doesnt_equal_credit.json"
    json_schema = "JSON_files/schemas/AA_STANDARD_schema.json"
    validation_result = Validator.validate_json(json_document, json_schema)
    print(validation_result)

    """Validate XML sample."""
    # xml_file = FileOperations.open_file(
    #     "app/files_with_errors/business_debitCreditCode_amount_3decimal_EE0302010.xml")
    # is_xml_valid = Validator.validate_xml(
    #     xml_file, "http://www.xbrl.org/taxonomy/int/gl/2015-03-25/plt/case-c-b-m/gl-plt-all-2015-03-25.xsd")
    # print("validation result: ", is_xml_valid)
    # errors = Validator.get_xml_validation_errors(
    #     xml_file, "http://www.xbrl.org/taxonomy/int/gl/2015-03-25/plt/case-c-b-m/gl-plt-all-2015-03-25.xsd")
    # print(errors)

    """Convert XML to JSON object and simple validation"""
    # data_from_xml_file = Converter.convert_xml_to_dict('XML_files/sample_reports/EE0301020_sample_report_stardard_small.xml')
    # clean = XBRLGLValidator.convert_xbrlglxml_to_dict(data_from_xml_file)
    # is_equal = XBRLGLValidator.compare_debit_credit(clean)
    # print(is_equal)

    """Generate bussiness rules json main->sub."""
    # xls_file = "JSON_files/import/Subaccount_limitations.xlsx"
    # raw_data = FileOperations.load_data_from_excel_return_dict(xls_file, "Sheet1", 0)
    # result = Converter.convert_xls_to_subaccount_limitations_json(raw_data)
    # FileOperations.save_dict_to_json_file(result, "subaccount_limitations")

    # # Converter.make_element_code_and_name_pairs('VG_112, VG_113, VG_114, VG_115, VG_116, VG_199', "VARAGRUPP2024ap")


if __name__ == "__main__":
    main()
