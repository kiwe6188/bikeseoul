# 따릉이 데이터셋 분석하기

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import glob
import os
import csv
import xlrd
from openpyxl import load_workbook

"""
# 1. 월별의 데이터를 1년으로 합치기
input_file = r'D:/dev/dataAnaysis project/sharedbike/seoul bike'
output_file = r'D:/dev/dataAnaysis project/sharedbike/seoul bike/bike_hour.csv'

# glob함수로 seoulbike_로 시작하는 파일들을 모은다
allFile_list = glob.glob(os.path.join(input_file, 'seoulbike_*'))
print(allFile_list)


allData = [] # 읽어들인 csv파일 내용을 저장할 빈리스트를 만든다.
for file in allFile_list:
    df = pd.read_csv(file)
    allData.append(df)

# concat함수를 이용해서 리스트의 내용을 병합
dataCombine = pd.concat(allData, axis=0, ignore_index=True)
# axis = 0은 수직병합, axis = 1은 수평병합. ignore_index=True는 기존 순서를 무시하고 순서대로 정렬
dataCombine.to_csv(output_file, index=False)
"""


input_file = r'D:/dev/dataAnaysis project/sharedbike/seoul bike/test'
output_file = r'D:/dev/dataAnaysis project/sharedbike/seoul bike/test/dust_hour1.csv'

# glob함수로 dust_로 시작하는 파일들을 모은다
allFile_list = glob.glob(os.path.join(input_file, 'dust_*'))
print(allFile_list)


allData = [] # 읽어들인 csv파일 내용을 저장할 빈리스트를 만든다.
for file in allFile_list:
    df = pd.read_csv(file, encoding='UTF-8')
    allData.append(df)

# concat함수를 이용해서 리스트의 내용을 병합
dataCombine = pd.concat(allData, axis=0, ignore_index=True)
# axis = 0은 수직병합, axis = 1은 수평병합. ignore_index=True는 기존 순서를 무시하고 순서대로 정렬
dataCombine.to_csv(output_file, index=False)
"""
# 1. csv파일을 분류해서 열기
input_path = r'D:/dev/dataAnaysis project/sharedbike/seoul bike'
output_path = r'D:/dev/dataAnaysis project/sharedbike/seoul bike/bike_hour.csv'

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'seoulbike_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_path, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False # 복사가 끝나면 첫번째 파일이 아니기 때문에 False로 한다.
            else:
                header = next(filereader)
                for row in filereader:
                    filewriter.writerow(row)
            print(filereader)
print('파일 합치기 성공')
"""