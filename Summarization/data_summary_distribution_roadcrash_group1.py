# Import libraries
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Count clases to view imbalance in the dataset which would introduce bias in the model
myClasscounts = myData.groupby('InjuryDesc').size()

# Print the class count
print()
print(myClasscounts)
print()