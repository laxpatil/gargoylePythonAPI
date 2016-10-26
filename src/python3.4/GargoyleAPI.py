#Python 3.4

import csv
import requests
import json


'''
Method used to get the JSON data as Python dict
'''
def getJSONdata(request,userId,apiKey):
    headers= {'userId':userId,'apiKey':apiKey}
    response = requests.get(request,headers=headers,verify=True) #need to be verified
    assert response.status_code == 200
    jsonData= response.json()
    return jsonData

'''
Method genrates a JSON file for the API request
'''
def getJSON(request,userId,apiKey,JSONFilePath):
    json_data=getJSONdata(request, userId, apiKey)
    with open(JSONFilePath, 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        print("Data is dumped to "+JSONFilePath+ " !")

'''
Method genrates a CSV file for the API request
'''
def getCSV(request,userId,apiKey,CSVFilePath):
    json_data=getJSONdata(request, userId, apiKey)
    data = json_data
    write_header = True
    item_keys = []
    with open(CSVFilePath, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        
        
        results=data['results']
        
        for item in results:
            item_values = []
            for key in item:
                if write_header:
                    item_keys.append(key)

                value = item.get(key)
                if isinstance(value, str):
                    item_values.append(value.strip().encode('utf-8'))
                else:
                    item_values.append(value)
                    #print(value)

            if write_header:
                writer.writerow(item_keys)
                write_header = False

            writer.writerow(item_values)
    print("Data is dumped to "+CSVFilePath+ " !")
    
    
'''
# HOW TO ACCESS THE ABOVE METHODS TO GET THE DATA AND GENERATE CSV

request='https://apigargoyle.com/GargoyleApi/getZerodayProducts?limit=100'
userId='user'
apiKey='e0c23066-6409035b-4a5b3-b0c0-c570b22d4069'
gargoyle.getCSV(request, userId, apiKey, "fileName.csv")
'''