import os
import openpyxl
import shutil

shutil.copy("H:\Mistakes\Excel Project\hospital_prospects.xlsx", 
        r"H:\Mistakes\Excel Project\test")

#test_list = ["a", "b", "c", "d", "e", "f"]

place_column = input('Prompt: ')
wb = openpyxl.load_workbook("hospital_prospects.xlsx")
ws = wb.active
place_name = ws[place_column].value
print(place_name)

for row in ws (min_row = 2, min_col = 2):
    for cell in row:
        count = 0
        while count <= len(test_list):
            cell.value == test_list[count]
            count += 1

#os.remove("hospital_prospects.xlsx")
