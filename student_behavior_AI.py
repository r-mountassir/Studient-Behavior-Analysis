import asyncio
import pandas as pd

import numpy as np
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import LabelEncoder
import joblib

dataset = pd.read_csv('Student_Data_Sample_Score.csv')
# dataset = dataset.drop(columns=['Unnamed: 0'])





students  = pd.DataFrame(
{
        'ID': dataset['Student_ID'].tolist(),
        'Math': dataset['Math_Score'].tolist(),
        'English': dataset['English_Score'].tolist(),
        'Science': dataset['Science_Score'].tolist(),
        'Absences': dataset['Absences'].tolist(),
        'Issues': dataset['Issues'].tolist(),
        'Social_Behavior': dataset['Social_Behavior'].tolist(),
        'Score_Str': dataset['Score_Str'].tolist()
})

le = LabelEncoder()

students['Behavior'] = le.fit_transform(students['Social_Behavior'])
students['Score'] = le.fit_transform(dataset['Score_Str'])


students.to_csv('students.csv')



X = students[['Math', 'English', 'Science', 'Absences', 'Issues', 'Behavior']]
y = students['Score']



X, y = make_classification(random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
regressor =  make_pipeline(StandardScaler(), LogisticRegression())
regressor.fit(X_train, y_train)
#regressor.score(X_test,y_test)

y_pred = regressor.predict(X_test)


new_student  = {

        'Math': 100,    #between 0 and 100
        'English': 100, #between 0 and 100
        'Science': 100, #between 0 and 100
        'Absences': 5,  #between 0 and 10
        'Issues': 6,    #between 0 and 10
        'Behavior': 2    #0=positive 1=average 2=negative
}


new_student = pd.DataFrame([new_student])

new_student_predect = regressor.predict(new_student)

convert = le.inverse_transform(new_student_predect)

print(f'Behavior new student is:  {convert[0]}')







