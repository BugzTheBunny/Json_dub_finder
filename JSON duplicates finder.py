import json

# json formatter - https://jsonformatter.curiousconcept.com/

# Base:
# File
json_file = 'filename' + '.json'
# File to compare with
catalog_file = 'otherfile.json'

# Variables to compare:
# Your file
check_for_name = 'key1'
check_for_url = 'key2'
# Catalog
catalog_check_for_name = 'key1'
catalog_check_for_url = 'key2'

# Json output file:
output_file = 'output.json'
###################__Json Files___############
with open(json_file, 'r') as data_json:
    json_data = json.load(data_json)

with open(catalog_file, 'r') as catalog:
    catalog_data = json.load(catalog)


def wtj(fileName, data):
    filePathNameWExt = fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


##############################################
catalog_size = len(catalog_data)
name_duplicates_counter = 0
url_duplicates_counter = 0
array = []

for obj in json_data:
    name = obj[check_for_name]
    old_url = obj[check_for_url]
    # url_fix
    url = old_url.replace('www2.', "")
    i = 0
    for data in catalog_data:
        if name == data[catalog_check_for_name]:
            info = {}
            info['name_a'] = name
            info['url_a'] = url
            info['name_b'] = data[catalog_check_for_name]
            info['url_b'] = data[catalog_check_for_url]
            name_duplicates_counter = name_duplicates_counter + 1
            print("Found duplicate by name")
            array.append(info)

    for data in catalog_data:
        if url == data[catalog_check_for_url]:
            info = {}
            info['name_a'] = name
            info['url_a'] = url
            info['name_b'] = data[catalog_check_for_name]
            info['url_b'] = data[catalog_check_for_url]
            url_duplicates_counter = url_duplicates_counter + 1
            print("Found duplicate by url")
            array.append(info)

wtj(output_file, array)
print(array)
print("Duplicates Found by Name: " + str(name_duplicates_counter))
print("Duplicates Found by URL: " + str(url_duplicates_counter))

#################	Json Generator ####################
