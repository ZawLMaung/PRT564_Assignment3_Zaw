# Import functions
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# read dataset
myDataframe = read_csv(myFilename, names=myNames)

# Extract the dataframe values
myArray = myDataframe.values

# Split the array into input and output
myExplanatoryvariables = myArray[:,0:23]
myResponsivevariable = myArray[:,23]

# Setup evaluation algorithm
myFolds = 100
myRandomseed = 0
myValidation = KFold(n_splits = myFolds, random_state = myRandomseed, shuffle = True)
myModel = KNeighborsClassifier()
myResult = cross_val_score(myModel, myExplanatoryvariables, myResponsivevariable, cv=myValidation)

# Print the accuracy of K-Neighbors
print()
print('Mean Estimated Accuracy K-Neighbors: %f ' % (myResult.mean()))
print()