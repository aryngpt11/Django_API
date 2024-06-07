#Read method
import requests
import json

URL = "http://127.0.0.1:8000/student_api/"

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
#get_data(3) #read method

#post

def post_data():
    data = {
        'name': 'arya',
        'roll': 27,
        'city': 'ballia'
    }
    headers={'content-Type':'application/json'}
    #convert in json data
    json_data=json.dumps(data)
    #sending rqst
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
#post_data()

#update

def update_data():
    data = {
        'id':5,
        'name': 'Ayush',
        'roll': '09'
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
        'id':1,
    }
    #convert in json data
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    #sending rqst
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
delete_data()


