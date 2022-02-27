#first is to import json

import json
import os
from typing import List, Dict

#Path to config.json file
CWD = os.getcwd()
JSON_CONFIG_FILE_PATH = '%s/%s' % (CWD, 'data.json')

#Dictionary holding config.json values

d = {}
# OPEN CONFIG.JSON, PARSE VALUES AND STORE THEM IN DICTIONARY

try:
    with open(JSON_CONFIG_FILE_PATH) as data_file:
        d = json.load(data_file)
        new_data = json.dumps(d, indent=2)
except IOError as e:
    print(e)
    print('IOError: Unable to open config.json.Terminating execution')
    exit(1)
print(new_data)
 # first function of getting type
def get_types(articles: str, tweets: str) -> List[Dict[str, str]]:
    return [{'name': articles, 'surname': tweets}]

#print(get_types('slug', 'Zappa'))

