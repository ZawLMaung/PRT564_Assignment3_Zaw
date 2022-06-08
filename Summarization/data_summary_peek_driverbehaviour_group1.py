# Import libraries
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingDriverBehaviourInliersData.csv'

# Define the data variable names
myNames = ['Experience', 'KlmsDist', 'Meter', 'Occupants', 'VehSeq', 'Airbag', 'AlcoholRel', 'LicClass', 'PedVMC',
           'HeavyVeh', 'Carriage', 'DUI', '4WD', 'Intername', 'LicStatus', 'NTRes', 'Community', 'Country', 'SafDevice',
           'Sex', 'State1', 'RegoState', 'RoadDivision', 'RoadName', 'RoadUser1', 'RoadWidth', 'Rural', 'SpeedRel',
           'SurfaceType', 'TSD', 'UnitType', 'VehMov', 'VehVMC', 'VertFeature', 'Weather', 'CyclistInv', 'ArticVeh1',
           'RigidVeh', 'ArticVeh2', 'ContFactor']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Print a quick preview of first 13 rows
myPeek = myData.head(13)
print()
print(myPeek)
print()