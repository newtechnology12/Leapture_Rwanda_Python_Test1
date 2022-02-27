## IMPORTS GO HERE
import json
import os
## END OF IMPORTS


### YOUR CODE FOR read_json_file() GOES HERE ###

#Path to config.json file
CWD = os.getcwd()
JSON_CONFIG_FILE_PATH = '%s/%s' % (CWD, 'data.json')

#Dictionary holding config.json values

d = {}
# OPEN CONFIG.JSON, PARSE VALUES AND STORE THEM IN DICTIONARY

try:
    with open(JSON_CONFIG_FILE_PATH) as data_file:
        d = json.load(data_file)
        d = json.dumps(d, indent=4)
except IOError as e:
    print(e)
    print('IOError: Unable to open config.json.Terminating execution')
    exit(1)
#print(d)
#### END OF MARKER


### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(dic):
    s = {}
    for i in dic:
        count = 0
        a = dic[i]
        for j in a:
            count += 1
        s[i] = count
    return s

#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
 # first function of getting type
def get_types(dic):
    lst = []
    for i in dic:
        lst.append(i)
    return lst

#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(dic, w):
    count = 0
    a = {}
    for i in dic:
        if type(dic) == list:
            for j in dic:
                count += 1
                break
            return count
        else:
            q = dic[i]
            for j in q:
                for k in j:
                    if k == "author":
                        a = j[k]
                for m in a:
                    b = a[m]

                    if b == w:
                        count += 1
    return count

#### End OF MARKER



if __name__ == '__main__':
    ### YOUR CODE FOR LOADING JSON DATA GOES HERE ###
    d = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
                "username": "jake",
                "bio": "I work at statefarm",
                "following": False
            }
        }, {
            "slug": "and another article",
            "body": "I'm getting bored",
            "tagList": ["bored", "article"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 20,
            "author": {
                "username": "cap",
                "following": True
            }
        }],
        "tweets": [{
            "body": "See my article on training mules.",
            "author": {
                "username": "jake"
            }
        }]
    }

   # d = read_json_file('data.json')

    #### End OF MARKER

    print("Dictionary: {}".format(d))


    # Call the functions and test your code
   # print( "get_types_counts(d): {}".format(get_types_counts(d)) )

    print("get_types(d): {}".format(get_types(d)))
    print("get_author_count(d, 'cap'): {}".format(get_author_count(d, 'cap')))
    print("get_author_count(d, 'jake', ['articles', 'tweets']): {}".format(get_author_count(d, 'jake')))

### END OF CODE