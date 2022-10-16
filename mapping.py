import json


import json
with open('300.txt', encoding='utf_8') as f:
    data = json.load(f)


reviews = data[2]
print (len(reviews))
data = []

for review in range(len(reviews)):
    if reviews[review][3] == "":
        body_review = "kosong"
        # print ('kosong')
    else:
        body_review = reviews[review][3]
        print (reviews[review][3])
    if reviews[review][0][1]:
        nama = reviews[review][0][1]
        # print (reviews[review][0][1])
    else:
        nama = "kosong"
        # print ('kosong')
    if reviews[review][4]:
        rating = reviews[review][4]
        # print (reviews[review][4])
    else:
        rating = "kosong"
        # print ('kosong')
    # print (
    #     [{
    #         "nama": nama,
    #         "body_review": str(body_review),
    #         "rating": rating
    #     }]
    # )
    data.append(
        {
        "nama": nama,
        "body_review": str(body_review),
        "rating": rating 
        }
    )

with open('300.json', 'w', encoding='utf_8') as outfile:
    json.dump(data, outfile)


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








# nama_reviewer = data[2][0][0][1]
