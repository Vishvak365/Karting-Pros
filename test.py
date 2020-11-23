# import numpy as np
# from numpy import load
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
import pickle

knn_filename = "knn_model.pkl"
with open(knn_filename, 'rb') as file:
    knn = pickle.load(file)
#[1,1,0,0]
print(knn.predict([[160,1616,677]]))