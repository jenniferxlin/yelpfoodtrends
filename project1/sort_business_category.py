import json

print('### Starting python script: Sort business category.')

with open('small_merged_business_checkin.json', 'r') as business_file:

    # Dict of dict with count
    category_state_count = {}
    business_data = json.load(business_file)
    for business in business_data:
        category_list = business['categories'].split(', ')
        state = business['state']
        for category in category_list:
            if category in category_state_count:
                if state in category_state_count[category]:
                    category_state_count[category][state] += 1
                else:
                    category_state_count[category][state] = 1
            else:
                category_state_count[category] = {state: 1}

    # Write to json file
    print('### Writting json to file.')
    with open('yelp_category_state_count.json', 'a') as append_file:

        print('### Opened write file.')
        append_file.write('[')
        for business_obj in category_state_count[:num_obj-1]:
            json.dump(business_obj, append_file)
            append_file.write(',\n')
        json.dump(category_state_count[num_obj-1], append_file)
        append_file.write(']')
