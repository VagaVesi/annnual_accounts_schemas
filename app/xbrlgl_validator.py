from decimal import Decimal

DATASET_BALANCE_MICRO_ENTITY = 'EE0301010'
DATASET_BALANCE_STANDARD_ENTITY = 'EE0301020'
DATASET_CHANGES_STANDARD_ENTITY = 'EE0302010'

class XBRLGLValidator:
    """Validate XBRL-GL xml data.
    
    functions:
    convert_xbrlglxml_to_dict: Make json object from xbrl-gl instance
    compare_debit_credit: Simple validation (comparsion)
    """

    def convert_xbrlglxml_to_dict(source_data: dict) -> dict:

        result = {"header":
                  {"uniqueID": source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-cor:uniqueID'],
                   'creationDate': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-cor:creationDate'],
                   'creator': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-bus:creator'],
                   'periodCoveredStart': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-cor:periodCoveredStart'],
                   'periodCoveredEnd': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-cor:periodCoveredEnd'],
                   'sourceApplication': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-bus:sourceApplication'],
                   'organizationIdentifier': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:entityInformation']['gl-bus:organizationIdentifiers']['gl-bus:organizationIdentifier'],
                   'defaultCurrency': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:documentInfo']['gl-muc:defaultCurrency'],
                   'dataset': source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:entryHeader']['gl-cor:entryNumber']
                   }, "details": []
                  }
        entries = source_data['xbrli:xbrl']['gl-cor:accountingEntries']['gl-cor:entryHeader']['gl-cor:entryDetail']

        if result['header']['dataset'] == DATASET_BALANCE_MICRO_ENTITY:
            for i in range(0, len(entries)):
                entry = {'lineNumberCounter': entries[i]['gl-cor:lineNumberCounter'],
                         'accountMainID': entries[i]['gl-cor:account']['gl-cor:accountMainID'],
                         'debitCreditCode': entries[i]['gl-cor:debitCreditCode'],
                         'amount': entries[i]['gl-cor:amount']
                         }
                result["details"].append(entry)
        return result

    def compare_debit_credit(source_data_formatted: dict) -> Decimal:
        """Compare Debit and Credit total amounts.
        
        arg: data from xml converter to dict 
        return(decimal): difference debit_total-credit_total
        """
        
        elements = source_data_formatted['details']
        debit_total = Decimal(2)
        credit_total = Decimal(2)
        for element in elements:
            if element['debitCreditCode'] == 'D':
                debit_total = debit_total + Decimal(element['amount'])
            else:
                credit_total = credit_total + Decimal(element['amount'])
        return debit_total - credit_total
