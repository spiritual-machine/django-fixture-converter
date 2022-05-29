## What does this script do?
This script takes data from an Airtable table and formats it into a Django fixture file.

## Dependencies
To use this script, you will need to ensure that you have the Airtable Python Wrapper and dotenv installed. You can do this by running:


```pip install airtable-python-wrapper python-dotenv```

## Configuration and Use
To use this script, you will need to create a ```.env``` environment file to define certain variables. Copy and past this into your file and fill in the details as needed:

```
# This is your private Airtable user token. DO NOT SHARE IT WITH ANYONE.
AIRTABLE_USER_TOKEN = "yourkeyhere"

# You can find your database and table ID by going through this: https://airtable.com/api
AIRTABLE_BASE_ID = "yourbaseidhere"

AIRTABLE_TABLE_ID = "yourtableidhere"

# This is where raw data from the Airtable will be dumped. Include the .json extension.
RAW_DATA_OUTFILE_NAME = "rawdatafile.json"

# This is where the fixture-formatted data will be dumped to. Include the .json extension.
FIXTURE_OUTFILE_NAME = "fixtureoutfile.json"

# This is your Django model as defined through your code. Typically the application name comes first, then the model name.
MODEL_NAME = "myapp.mymodel"
```
Some of these variables really don't *need* to be put into a .env file, but this keeps configuration localized and easy.

## Example
Airtable view:
![image](https://user-images.githubusercontent.com/100234759/170846996-4d1bda5b-d439-4b1a-9ce0-0457ede5524e.png)

Raw data output:
```
  {
    "id": "recDQN1EWFFBY9s7y",
    "createdTime": "2022-05-29T00:24:45.000Z",
    "fields": {
      "Name": "Wednesday",
      "Something Fun": "purrs a lot",
      "Something Unfun": "very fat never moves",
      "Rating": 4,
      "Species": "Cat",
      "Birthday": "2015-12-14"
    }
  },
  {
    "id": "recX78gMm5wWhnYul",
    "createdTime": "2022-05-29T00:24:45.000Z",
    "fields": {
      "Name": "Felix",
      "Something Fun": "perfect cat curl",
      "Something Unfun": "weird moustache",
      "Rating": 1,
      "Species": "Cat",
      "Birthday": "2014-08-04"
    }
  },
  {
    "id": "recaV9pQYVXqCVbVh",
    "createdTime": "2022-05-29T00:24:45.000Z",
    "fields": {
      "Name": "Lizzie",
      "Something Fun": "fuzzy",
      "Something Unfun": "poops on couch",
      "Rating": 3,      
      "Birthday": "2019-05-26",
      "Species": "Dog"
    }
  }
]
```

Django fixture:
```
[
  {
    "model": "petlist.pets",
    "pk": 1,
    "fields": {
      "name": "Wednesday",
      "something_fun": "purrs a lot",
      "something_unfun": "very fat never moves",
      "rating": 4,
      "species": "Cat",
      "birthday": "2015-12-14"
    }
  },
  {
    "model": "petlist.pets",
    "pk": 2,
    "fields": {
      "name": "Felix",
      "something_fun": "perfect cat curl",
      "something_unfun": "weird moustache",
      "rating": 1,
      "species": "Cat",
      "birthday": "2014-08-04"
    }
  },
  {
    "model": "petlist.pets",
    "pk": 3,
    "fields": {
      "name": "Lizzie",
      "something_fun": "fuzzy",
      "something_unfun": "poops on couch",
      "rating": 3,
       "birthday": "2019-05-26",
      "species": "Dog"
    }
  }
]
