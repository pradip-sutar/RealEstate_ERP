a = {
    'company_detail[companyid]': ['100'],
    'company_detail[name]': ['ABC Corp'],
    'brand_detail[companyid]': ['100'],
    'brand_detail[brand_name]': ['XYZ Brand'],
    'location_detail[city]': ['New York']
}

# Initialize empty dictionaries for each prefix
company_json = {}
brand_json = {}
location_json = {}

# Iterate through the dictionary
for key, value in a.items():
    # Check the prefix and populate corresponding JSON data
    if key.startswith('company_detail'):
        field = key.split('[')[1][:-1]  # Extract the field inside []
        company_json[field] = value[0]  # Use the first value in the list
    elif key.startswith('brand_detail'):
        field = key.split('[')[1][:-1]
        brand_json[field] = value[0]
    elif key.startswith('location_detail'):
        field = key.split('[')[1][:-1]
        location_json[field] = value[0]

# Print or use the resulting JSONs
print("Company JSON:", company_json)
print("Brand JSON:", brand_json)
print("Location JSON:", location_json)
