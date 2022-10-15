import json


import json
with open('300.txt', encoding='utf_8') as f:
    data = json.load(f)

# cari body review
# for i in range(len(data[2])):
#     if data[2][i][3] == "":
#         print ('kosong broo')
#     else:
#         print (data[2][i][3])

































# cari rating
# for i in range(len(data[2])):
#     print (data[2][i][4])

# # cari nama
# for i in range(len(data[2])):
#     print (data[2][i][0][1])





























nama_reviewer = data[2][0][0][1]
