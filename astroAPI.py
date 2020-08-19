import requests
import json
import csv

#Request the JSON from the API and print it out the Response Status to the screen
astros = requests.get('http://api.open-notify.org/astros.json')
print('Request Status:', astros.status_code)

#Create the python object 'people_json' (line9) and print it to the screen (line10)
astros_json = astros.json()
print("JSON Response:\n",astros_json)

#From the JSON object created on line 9, print the value stored in the 'number' key
print("Number of people in space:",astros_json['number'])

#To print the names of people in space using a for loop
for p in astros_json['people']:
    print('Astronaut Name: {} \t Craft: {}'.format(p['name'],p['craft']))

#---Code below is attempting to save the output in a txt file. Not working because of TypeError JSON object must be str, not dict
dict = astros_json
w = csv.writer(open("testAstro.csv", "w"))
for key, val in dict.items():
    w.writerow([p])

#Other ways to save json output in a file (these also haven't worked)
#writeMe = json.loads(p)
#saveFile = open('astrosList.txt','a')
#saveFile.write(writeMe)
#saveFile.close()

#file = open("rTest.txt", "w")
#file.write(test)
#file.close()

#with open('dataTest.txt', 'w') as outfile:
# json.dump(test, outfile)

#files = json.loads(text)
#saveFile = open('testData.csv','w')
#saveFile.write(files)
#saveFile.close()