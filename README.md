# CSV2Excel
This utility converts a csv file and updates data in workday EIB sample xlsx.

## Installation

cd to root directory and install requirements.txt

```bash
pip install -r requirements.txt
```

OR

Run:
```bash
pip install csvfile
pip install openpyxl
```

## Usage
cd to the root directory and from the command-line run:
```bash
python csv2excel.py {path_to_csv.csv}
```

Output file will be saved at the same path with a suffix of "-output.xlsx"