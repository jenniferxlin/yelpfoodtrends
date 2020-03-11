import json

print('### Starting python script: Filter restaurants.')

with open('yelp_modified_dataset_business.json', 'r') as business_file:

    # array with only restaurants
    filtered_data = []
    business_data = json.load(business_file)
    for business in business_data:
        category_list = []
        if business['categories']:
            category_list = business['categories'].split(', ')
        if 'Restaurants' in category_list:
            filtered_data.append(business)

    # Write to json file
    print('### Writting json to file.')
    with open('yelp_restaurants.json', 'a') as append_file:
        print('### Opened write file.')
        num_obj = len(filtered_data)
        append_file.write('[')
        for business_obj in filtered_data[:num_obj-1]:
            json.dump(business_obj, append_file)
            append_file.write(',\n')
        json.dump(filtered_data[num_obj-1], append_file)
        append_file.write(']')

print('### Done.')
