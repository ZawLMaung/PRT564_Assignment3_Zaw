# Import functions
import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
from scipy.stats import mode
from sklearn.metrics import accuracy_score

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# read dataset
myDataframe = pd.read_csv(myFilename, names=myNames)

# Build K-Means clustering model with 7 clusters
myClasses = 7
myRandomseed = 0
myModel = KMeans(n_clusters=myClasses, max_iter=100, random_state=myRandomseed)
myClusters = myModel.fit_predict(myDataframe.iloc[:,0:23])

# Function to map K-Means cluster labels to actual class labels
def map_cluster_to_class(cluster, cls, k):
        labels = np.zeros_like(cluster)
        for i in range(k):
                mask = (cluster == i)
                labels[mask] = mode(cls[mask])[0]
        return labels

# Map cluster labels to class labels
myClusters = map_cluster_to_class(myClusters, myDataframe.InjuryDesc, myClasses)

# Store the responsive variable values
myClassValues = myDataframe.InjuryDesc.values

# Print the accuracy of K-Means Clustering
print()
print("Overall K-Means accuracy %.2f%%" % (accuracy_score(myClassValues, myClusters) * 100))
print()