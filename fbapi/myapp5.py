#Read method
import requests
import json

URL = "http://127.0.0.1:8000/hello_world/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        #python to json data
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r = requests.get(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
#get_data() #read method

#post

def post_data():
    data = {
        'name': 'arya',
        'roll': 250,
        'city': 'ballia'
    }
    headers={'content-Type':'application/json'}
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
post_data()

#update

def update_data():
    data = {
        'id':4,
        'name': 'Sanjay',
        'city': 'Khejuri'
    }
    headers={'content-Type':'application/json'}
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
#update_data()

#Delete

def delete_data():
    data = {
        'id':3,
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
#delete_data()


