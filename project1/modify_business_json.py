import json

print('### Starting python script.')

print('### Loading json file.')
business_l = []
for line in open('yelp_academic_dataset_business.json', 'r'):
    business_l.append(json.loads(line))

print('### Loaded json file.')
num_obj = len(business_l)
for business_idx in range(num_obj):
    del business_l[business_idx]['hours']
    del business_l[business_idx]['attributes']
    del business_l[business_idx]['address']
    del business_l[business_idx]['latitude']
    del business_l[business_idx]['longitude']

print('### Writting json to file.')
with open('yelp_modified_dataset_business.json', 'a') as append_file:
    print('### Opened write file.')
    append_file.write('[')
    for business_obj in business_l[:num_obj-1]:
        if (business_obj['is_open']):
            json.dump(business_obj, append_file)
            append_file.write(',\n')
    json.dump(business_l[num_obj-1], append_file)
    append_file.write(']')

print('### Done! Check out the file size.')
