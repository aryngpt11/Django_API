#Read method
import requests
import json 

URL = "http://127.0.0.1:8000/StudentAPI/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        #python to json data
    json_data=json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
#get_data(2) #read method

#post

def post_data():
    data = {
        'name': 'Arav',
        'roll': 8,
        'city': 'Khejuri'
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
#post_data()

#update

def update_data():
    data = {
        'id':8,
        'name': 'Aarav',
        'roll':29,
        'city': 'BUI'
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
update_data()

#Delete

def delete_data():
    data = {
        'id':7,
    }
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
#delete_data()


