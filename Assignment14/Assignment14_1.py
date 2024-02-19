import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def PlayPredictor(model_name):
    predicted = model_name.predict([[0,2]])
    print("Predicted outcome is",predicted)
    

def CheckAccuracy(file_path):
    data = pd.read_csv(file_path, index_col = 0)
  
    feature_names = ['Whether','Temperature']

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    le = preprocessing.LabelEncoder()

    weather_encoded = le.fit_transform(whether)
  
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)
    
    features = list(zip(weather_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(features,label)
    PlayPredictor(model)
    
    data_train,data_test,target_train,target_test = train_test_split(features,label,test_size=0.5,shuffle=False)
   
    predicted = model.predict(data_test)

    Accuracy = accuracy_score(target_test,predicted)
    print("Accuracy of the model is ",Accuracy*100,"%")


def main():
    File = "PlayPredictor.csv"
    CheckAccuracy(File)

if __name__=="__main__":
    main()
