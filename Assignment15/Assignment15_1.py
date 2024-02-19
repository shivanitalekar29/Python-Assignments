import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv("WinePredictor.csv")

# Step 2: Data Preparation (Explore, Clean, Preprocess)
                                                                                                                                                                
# Step 3: Data Splitting               
X = data.drop('Class',axis=1)   # Features                                                                                      
y = data['Class']              # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# Step 4: Feature Selection (optional)
                                                                                                  
# Step 5: Model Building
k = 3  # Number of neighbors
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy*100)

# Step 7: Hyperparameter Tuning (optional)

# Step 8: Visualization (optional)
