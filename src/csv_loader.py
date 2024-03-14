"""
module: This module loads a given csv file and converts it into a json
"""
from pathlib import Path
import csvfile
import xlsxwriter

def build(fname: str):
    """
    loads given csv file into object by calling __load_csv().
    """
    try:
        records = __load_csv(fname)

        if len(records) == 0:
            print("no records found, aborting creating excel file.")
            return

        __print_log(f'loaded {len(records)} records from {fname}')

        __write_to_excel(fname, records)
        __print_log("Successfully created xlsx")

    except Exception as error:
        print(error.args)

# private functions
def __load_csv(fname: str):
    rows = csvfile.load(fname)
    return rows

def __write_to_excel(fname: str, records: list):
    if len(records) == 0:
        return False
    
    fname = Path(fname)
    xlsx_fname = fname.with_suffix('.xlsx')
    __print_log(f"creating {xlsx_fname}")

    workbook = xlsxwriter.Workbook(xlsx_fname)
    worksheet = workbook.add_worksheet('Change Job')
    # formatting
    bold = workbook.add_format({'bold': True})

    row = 1
    col = 0

    for record in records:
        for key in record:

            if row == 1:
                worksheet.write(row, col, key, bold)

            worksheet.write(row+1, col, record[key])
            col +=1
        row += 1

    workbook.close()

    return True

def __print_log(*logs):
    text = ""
    for log in logs:
        text += str(log)
    print("*********", text, "*********")
