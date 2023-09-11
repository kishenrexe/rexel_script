from openpyxl import load_workbook


wb = load_workbook(filename="EC000014.xlsx")
print(wb)
test = wb.get_sheet_names()

sheet = wb.get_sheet_by_name(test[0])
print(test)
print(sheet)

columns = "ABCDE"

for element in columns:
    print(sheet[f'{element}1'].value,end=' ')


def setworksheets() :
    