# Import libraries
from pandas import read_csv
from pandas import set_option

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Set printing options
set_option('display.width', 250)
set_option('display.max_columns', 15)
set_option('precision', 3)

# Print data description
myDescription = myData.describe()
print()
print(myDescription)
print()