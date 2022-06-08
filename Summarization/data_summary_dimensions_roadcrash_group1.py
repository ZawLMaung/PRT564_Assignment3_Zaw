# Input Libraries
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Print the shape of the dataset
myShape = myData.shape
print()
print(myShape)
print()