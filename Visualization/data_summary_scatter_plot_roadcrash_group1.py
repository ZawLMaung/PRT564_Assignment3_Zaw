# Input libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# Read csv file
myData = read_csv(myFilename, names=myNames)

# Print scatter plot
scatter_matrix(myData, color='blue')
plt.show()