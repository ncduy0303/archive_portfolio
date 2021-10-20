import xlrd
import re
import json

def is_valid_module(row, offset):
    code = row[offset].value
    grade = row[offset + 3].value
    if not re.match(r"[A-Z]{2,3}[0-9]{4}[A-Z]?", code):
        return False
    if grade == '':
        return False
    return True


def get_module(row, offset):
    code = row[offset].value
    description = row[offset + 1].value
    grade = row[offset + 3].value
    module = {
        "code": code,
        "description": description,
        "grade": grade
    }
    return module


workbook = xlrd.open_workbook('Graduation Requirements.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1

modules = []
codes = set()

def f(row, offset):
    if is_valid_module(row, offset):
        module = get_module(row, offset)
        if module["code"] in codes:
            return
        codes.add(module["code"])
        modules.append(module)

for i in range(num_rows):
    row = worksheet.row(i)
    f(row, 0)
    f(row, 12)

modules = sorted(modules, key=lambda x: x["code"])
cs_modules = []
ma_modules = []
other_modules = []
for module in modules:
    if re.match(r"(CS)[0-9]{4}[A-Z]?", module["code"]):
        cs_modules.append(module)
    elif re.match(r"(MA|ST)[0-9]{4}[A-Z]?", module["code"]):
        ma_modules.append(module)
    else:
        other_modules.append(module)
print(json.dumps(cs_modules))
print()
print(json.dumps(ma_modules))
print()
print(json.dumps(other_modules))
