#####################################################################################
# A script for downloading Airtable data into a formatted Django fixture file.      #
# Please read the README.md for information on how to configure this script!        #
#                                                                                   #
# Written by Autumn Denny                                                           #
# https://github.com/Autumn-Denny/django-fixture-converter                          #
#####################################################################################

import os
from dotenv import load_dotenv
from airtable import Airtable
from pprint import pprint
import json

# Load everything we need from the .env we made.
load_dotenv()

airtableToken = os.getenv('AIRTABLE_USER_TOKEN')
airtableBaseID = os.getenv('AIRTABLE_BASE_ID')
airtableTableID = os.getenv('AIRTABLE_TABLE_ID')
# These don't technically *need* to be added as an environmental variable, but I'd rather keep all the configuration in one place.
fixtureFile = os.getenv('FIXTURE_OUTFILE_NAME')
rawFile = os.getenv('RAW_DATA_OUTFILE_NAME')
modelName = os.getenv('MODEL_NAME')



# Setting values for the Airtable class instance
airtable = Airtable(airtableBaseID, airtableTableID, airtableToken)



# Let's pull all the fields from the Airtable
data = airtable.get_all()



# Dumps all the raw data from Airtable into a raw data JSON file (just for logging purposes and such).
jsonObject = json.dumps(data, indent = 2)
with open (rawFile,"w") as outfile:
	outfile.write(jsonObject)



# Initializing an ID variable that will be used for the "pk" fixture value.
id = 0



# We also need to initialize an empty list to store our data.
dataList = []



# Okay, so now we have a list. Some of the values (like "fields") are dictionaries within the list.
for record in range(len(data)):
	id += 1 # Add one to ID for the 'pk' value
        # Creating a temporary dictionary with the model name, pk/id, and the fields we got from Airtable
	tempDict = {
		"model": modelName,
		"pk": id,
		"fields": data[record]["fields"]
	}
	# Append the temporary dictionary to the data list that will be dumped into the fixture.
	dataList.append(tempDict)



# Dumps out to the json file as configured.
jsonObject = json.dumps(dataList, indent = 2)
with open(fixtureFile, "w") as outfile:
	outfile.write(jsonObject)


# Yay! We did it!
print("Success! " + str(id) + " records found and added to " + fixtureFile + "as a Django fixture file.")
print("Raw data was dumped into " + rawFile)
