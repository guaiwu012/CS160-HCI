import openpyxl
import random
import numpy as np
import json
grading = []  

workbook = openpyxl.load_workbook('emotion_grading.xlsx')
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    unicode_code = row[0]  
    six_numbers = []
    for cell in row[2:8]:
        splitted = str(cell).split("-")
        first_number = float(splitted[0])  # 第一个数字
        second_number = float(splitted[1])  # 第二个数字
        six_numbers.extend([first_number, second_number])
    data = (unicode_code, six_numbers)  # 将数据打包为元组
    grading.append(data)

workbook.close()

#print(grading[0][1][0])
#print(len(grading))
with open("output.txt", "r", encoding="utf-8") as input_file:
    data = input_file.read()
data_json = json.loads(data)
sentences = data_json["Result"]["Sentences"]
extracted_text = [sentence["Text"] for sentence in sentences]
print(extracted_text)
numbers = [] 
possible = []
with open("scores.txt", "r") as file:
    lines = file.readlines()
    lines.remove(lines[0]) 
    numbers=np.loadtxt(lines, delimiter=" ", dtype=float)
    #print(numbers)
    for j in range(len(numbers)):
        for i in range(len(grading)):
            if (numbers[j][0]>=grading[i][1][0] and numbers[j][0]<=grading[i][1][1] and numbers[j][1]>=grading[i][1][2] and numbers[j][1]<=grading[i][1][3] and numbers[j][2]>=grading[i][1][4] and numbers[j][2]<=grading[i][1][5] and numbers[j][3]>=grading[i][1][6] and numbers[j][3]<=grading[i][1][7] and numbers[j][4]>=grading[i][1][8] and numbers[j][4]<=grading[i][1][9] and numbers[j][5]>=grading[i][1][10] and numbers[j][5]<=grading[i][1][11]):
                possible.append(grading[i][0])
        with open("final.txt", "a", encoding="utf-8") as file:
            file.write(extracted_text[j])
            if (possible != []):
                file.write(random.choice(possible)+'\n')
        




#print("\U0001F604")
