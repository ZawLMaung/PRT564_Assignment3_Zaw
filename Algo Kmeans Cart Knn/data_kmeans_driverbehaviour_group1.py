# Import functions
import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
from scipy.stats import mode
from sklearn.metrics import accuracy_score

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingDriverBehaviourInliersData.csv'

# Define the data variable names
myNames = ['Experience', 'KlmsDist', 'Meter', 'Occupants', 'VehSeq', 'Airbag', 'AlcoholRel', 'LicClass', 'PedVMC',
           'HeavyVeh', 'Carriage', 'DUI', '4WD', 'Intername', 'LicStatus', 'NTRes', 'Community', 'Country', 'SafDevice',
           'Sex', 'State1', 'RegoState', 'RoadDivision', 'RoadName', 'RoadUser1', 'RoadWidth', 'Rural', 'SpeedRel',
           'SurfaceType', 'TSD', 'UnitType', 'VehMov', 'VehVMC', 'VertFeature', 'Weather', 'CyclistInv', 'ArticVeh1',
           'RigidVeh', 'ArticVeh2', 'ContFactor']

# read dataset
myDataframe = pd.read_csv(myFilename, names=myNames)

# Build K-Means clustering model with 5 clusters
myClasses = 5
myRandomseed = 0
myModel = KMeans(n_clusters=myClasses, max_iter=100, random_state=myRandomseed)
myClusters = myModel.fit_predict(myDataframe.iloc[:,0:39])

# Function to map K-Means cluster labels to actual class labels
def map_cluster_to_class(clus, cls, k):
        labels = np.zeros_like(clus)
        for i in range(k):
                mask = (clus == i)
                labels[mask] = mode(cls[mask])[0]
        return labels

# Map cluster labels to class labels
myClusters = map_cluster_to_class(myClusters, myDataframe.ContFactor, myClasses)

# Store the responsive variable values
myClassValues = myDataframe.ContFactor.values

# Print the accuracy of K-Means Clustering
print()
print("Overall K-Means accuracy %.2f%%" % (accuracy_score(myClassValues, myClusters) * 100))
print()