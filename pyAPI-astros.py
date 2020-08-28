import requests
import pandas


print('Begin Code')
#Request the JSON from the API and print it out the Response Status to the screen
astros = requests.get('http://api.open-notify.org/astros.json')
print('Request Status:', astros.status_code)

#Create the object 'astros' (line11) and print it to the screen (line12)
astros_json = astros.json()
print("JSON Response:\n",astros_json)

#From the JSON object created on line 9, print the value stored in the 'number' key
print("Number of people in space:",astros_json['number'])

# the code below accesses child objects (dicts)
df = pandas.json_normalize(astros_json["people"])

print(df)
df.to_csv('/Users/noah.griego/Desktop/TMSECNA/Internal/NJG/Python/dataGathering/pythonAPI/astroTestOutput.csv', index = None)