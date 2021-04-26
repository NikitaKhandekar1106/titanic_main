import pickle
import json
import numpy as np

model=pickle.load(open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\titanic\titanic_train.pickle','rb'))

def get_age_groups():
    with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\titanic\titanic.json','r')as f:
        age_groups=json.load(f)['data_columns']
        return ages_groups[1]

def get_survived_predict(age,pclass,male):
    if age in range(1,100):
        if male==1:
            return('survived male')
        else:
            return('survived female')
    else:
        return('invalid age')

if __name__=='__main__':
    print(get_survived_predict(22,3,1))
    print(get_survived_predict(38,1,0))



