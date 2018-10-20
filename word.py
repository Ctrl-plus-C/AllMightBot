import requests
import json
import os

def words(word_s):
    app_id = os.environ.get('word_id')
    app_key = os.environ.get('word_key')

    language = 'en'
    word_id = word_s

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/search/' + language + '?q=' + word_id.lower() + '&prefix=false'

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}).json()
    mylist = []
    # print(r["results"])
    for w in r["results"]:
        # print(w)
        mylist.append(w["word"])
    
    a = ' '.join(mylist)
    # print(a)
    return a

# def main():
#     # words()
#     print(words())

# main()
# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# # print("json \n" + json.dumps(r.json()))