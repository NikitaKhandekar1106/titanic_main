import pickle,json
import numpy as np

data_cols=None
model=None

def load_saved_artifacts():
    print('loading saved artifacts...........started......')
    global model,data_cols
    with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\titanic\titanic.json','r')as f:
        data_cols=json.load(f)['data_columns']
        
        if model is None:
            with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\titanic\titanic_train.pickle','rb')as f:
                model=pickle.load(f)
                
    print('loading saved artifacts...........done')

def survived_predict(age,pclass,male):
    if age in range(1,100):
        if male==1:
            return('survived male')
        else:
            return('survived female')
    else:
        return('invalid age')

if __name__=='__main__':
    print(survived_predict(38,1,0))
    print(survived_predict(0,0,0))

