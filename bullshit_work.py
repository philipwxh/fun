import csv
from bson.objectid import ObjectId

filename="test.csv"
list_of_dict= []

with open(filename, 'r') as file:
   reader = csv.DictReader(file)
   data_dict = [row for row in reader]


data_list = []
for item in data_dict:
    item = dict(item)
    item["id"] = ObjectId()
    item["paired"]=False
    data_list.append(item)

# for item in data_list:
#     print(item)

KEY_TO_CHECK = ["Name", "Account", "Memo"]
def data_match(data1:dict, data2:dict):
    for key in KEY_TO_CHECK:
        if data1[key]!= data2[key]:
            return False
    if float(data1["Amount"]) != -float(data2["Amount"]):
        return False
    return True


pairs = []
for idx1 in range(len(data_list)):
    data1 = data_list[idx1]
    if data1["paired"]:
        continue
    for idx2 in range(idx1+1, len(data_list)):
        data2 = data_list[idx2]
        if data2["paired"]:
            continue
        if data_match(data1, data2):
            pairs.append(data1)
            pairs.append(data2)
            data1["paired"]=True
            data2["paired"]=True
            break

# print("\n\n\n")
# for item in pairs:
#     print(item)

keys = pairs[0].keys()
with open('pairs.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pairs)
