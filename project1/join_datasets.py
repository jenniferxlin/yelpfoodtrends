import json

print('### Starting python script: Join datasets.')

business_l = []
id_to_index = {}

print('### Loading first json file.')
with open('yelp_modified_dataset_business.json', 'r') as business_file:

    print('### Loading second json file.')
    with open('yelp_modified_dataset_checkin.json', 'r') as checkin_file:
        business_data = json.load(business_file)
        checkin_data = json.load(checkin_file)
        i = 0

        # build inverted index
        num_obj = len(business_data)
        for b_idx in range(num_obj):
            b_id = business_data[b_idx]['business_id']
            id_to_index[b_id] = b_idx
            business_data[b_idx]['num_checkins'] = 0

        # merge lists
        i = 0
        for checkin in checkin_data:
            b_id = checkin['business_id']
            if b_id in id_to_index:
                b_idx = id_to_index[b_id]
                business_data[b_idx]['num_checkins'] = checkin['num_checkins']
            if i % 10000 == 0:
                print(i)
            i += 1

        # Write to json file
        print('### Writting json to file.')
        with open('yelp_merged_business_checkin.json', 'a') as append_file:

            print('### Opened write file.')
            append_file.write('[')
            for business_obj in business_data[:num_obj-1]:
                json.dump(business_obj, append_file)
                append_file.write(',\n')
            json.dump(business_data[num_obj-1], append_file)
            append_file.write(']')

print('### Done! Check file size.')
