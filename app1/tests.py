import requests
import csv
import json
import urllib3

<<<<<<< HEAD


file_path = "D:\\GEGDC\\SP815975\\Others\\ActivityLogs.csv"
 
data = []
username = "CAI_Service_Ops_User"
password = "EDM@InfaCAI2024Ops"
 
csv_file_path = "D:\\GEGDC\\SP815975\\Others\\ActivityLogs.csv"
 
def get_session_id():
    login_api_url = "https://dm-us.informaticacloud.com/ma/api/v2/user/login"
    credentials = {
        "username": username,
        "password": password
    }
    login_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
 
    login_response = requests.request("POST", login_api_url, json=credentials, headers=login_headers)
    print('Login API executed - ' + login_api_url)
    return login_response.json()
 
response_data=get_session_id()
 

sessionID=response_data['icSessionId']
Base_url=response_data['serverUrl']
print(sessionID)
print(Base_url)
 

def all_activity_log():
    url=Base_url +"/api/v2/activity/activityLog"
    credentials = {
        "username": username,
        "password": password
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "icSessionId": sessionID
    }
    response = requests.request("GET", url, json=credentials, headers=headers)
    return response.json()
    
 
json_data=all_activity_log()
 
csv_data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        csv_data.append(row)
 

json_id_field = 'startTime'
csv_id_column_index = 6  # Assuming ID is in the first column
 
matched_data = []
 
for json_entry in json_data:
    json_id = json_entry[json_id_field]  # Adjust according to JSON structure
    for csv_row in csv_data:
        csv_id = csv_row[csv_id_column_index]  # Adjust according to CSV structure
        if json_id == csv_id:
            matched_data.append((json_entry, csv_row))
            break  # Assuming IDs are unique, break if match found
 
# matched_data now contains tuples of matched JSON and CSV entries
 
csv_file_path2 = "D:\\GEGDC\\SP815975\\Others\\ActivityLogs2.csv"
 

print(matched_data[0])
 
with open(csv_file_path2, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(matched_data)
 
print(f'CSV file "{csv_file_path2}" has been successfully created with the data.')
=======
# Create your tests here.
>>>>>>> f03eeb3825fb507ec3414d98915f2dedd3f7c74b
