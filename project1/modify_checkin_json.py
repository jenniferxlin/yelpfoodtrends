import json

print('### Starting python script.')

print('### Loading json file.')
business_l = []
for line in open('yelp_academic_dataset_checkin.json', 'r'):
    business_l.append(json.loads(line))

print('### Loaded json file.')
num_obj = len(business_l)
for business_idx in range(num_obj):
    dates_list = business_l[business_idx]['date'].split(",")
    business_l[business_idx]['num_checkins'] = len(dates_list)
    del business_l[business_idx]['date']

print('### Writting json to file.')
with open('yelp_modified_dataset_checkin.json', 'a') as append_file:
    print('### Opened write file.')
    append_file.write('[')
    for business_obj in business_l[:num_obj-1]:
        json.dump(business_obj, append_file)
        append_file.write(',\n')
    json.dump(business_l[num_obj-1], append_file)
    append_file.write(']')

print('### Done! Check out the file size.')
