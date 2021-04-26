from pymongo import MongoClient

db_name="titanic_db"
myclient=MongoClient('mongodb://localhost:27017/')
db=myclient[db_name]
collection_passengers=db['passenger_details']
collection_survived=db['survived_details']

def register(passenger_data):
    passenger_dict={}
    passenger_dict['name']=passenger_data['name']
    passenger_dict['age']=passenger_data['age']
    passenger_dict['pclass']=passenger_data['pclass']
    passenger_dict['sex']=passenger_data['sex']

    collection_passengers.insert_one(passenger_dict)
    return "data entered successfully"

def login(login_data):
    passenger_dict={}
    passenger_dict['name']=login_data['name']
    passenger_dict['age']=login_data['age']
    passenger_dict['pclass']=login_data['pclass']
    passenger_dict['sex']=login_data['sex']

    response= collection_passengers.find_one(login_data)
    
    if not response:
        return 'invalid username or password'
    return 'successfully logged in'

def survived(age,pclass,male,prediction):
     survived_details={'age':age,'pclass':pclass,'male':male,'prediction':prediction}
     collection_survived.insert_one(survived_details)

     return 'success'