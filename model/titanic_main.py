import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report


df=pd.read_csv(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\titanic\titanic_train.csv')
print(df)

print(df.isnull().sum())

print(df.info())

df=df.drop(['PassengerId','Name','Ticket','Fare','Cabin'],axis=1)
print(df)

embarked=pd.get_dummies(df['Embarked'],drop_first=True)
print(embarked)

sex=pd.get_dummies(df['Sex'],drop_first=True)
print(sex)

df=pd.concat([df,sex,embarked],axis=1)
print(df)

df=df.drop(['Sex','Embarked'],axis=1)
print(df)

print(df.info())

print(df.isnull().sum())

df=df.fillna(df['Age'].median().astype('int64'))
print(df)

df.isnull().sum()
###############################################################################
x=df.drop('Survived',axis=1)
y=df['Survived']
##############################################################################
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

hyperparameters={'criterion':['gini','entropy'],'max_depth':list(range(2,10))}
##################################################################################

dtc=DecisionTreeClassifier()

best_model=GridSearchCV(dtc,hyperparameters,cv=5)
best_model.fit(x_train,y_train)
y_pred_best=best_model.predict(x_test)
print(best_model.best_params_)


print(best_model.score(x_test,y_test))

dtc.fit(x_train,y_train)

y_pred=dtc.predict(x_test)
print(y_pred)

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

plt.figure(figsize=(15,20))
plot_tree(decision_tree=dtc,rounded=True,filled=True,class_names=x.columns)
export_graphviz(dtc)

df.corr().abs()

sns.countplot(x='Pclass',hue='Survived',data=df)

sns.countplot(x='Age',hue='Survived',data=df)

sns.countplot(x='male',hue='Survived',data=df)

#####################################################################################################Sex

####################################### SAVING MODEL  #######################################

import pickle
model=[dtc]
with open('titanic_train.pickle','wb') as f:
    pickle.dump('dtc',f)

import json
columns = {
    'data_columns' : [col.lower() for col in x.columns]
}
with open("titanic.json","w") as f:
    f.write(json.dumps(columns))

