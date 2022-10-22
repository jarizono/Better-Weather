import requests
import csv
import codecs

resp = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Atlanta,GA?&unitGroup=us&contentType=csv&include=days&key=ESVDJCXR83MMMX2MQFC7FUGE6')
# print(resp.content)

CSVText = csv.reader(codecs.iterdecode(resp, 'utf-8'))
print(CSVText)

# RowIndex = 0
# weatherDict = {}
# for Row in CSVText:
#     if RowIndex == 0:
#         FirstRow = Row
#     else:
#         print('Weather in ', Row[0], ' on ', Row[1])
#         weatherDict[Row[1]] = []

#         ColIndex = 0
#         for Col in Row:
#             if ColIndex >= 4:
#                 weatherDict[Row[1]].append(FirstRow[ColIndex])
#                 weatherDict[Row[1]].append(Row[ColIndex])
#                 #print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
#             ColIndex += 1
#     RowIndex += 1