# Input libraries
from matplotlib import pyplot as plt
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingDriverBehaviourInliersData.csv'

# Define the data variable names
myNames = ['State1', 'RegoState', 'RoadDivision', 'RoadName', 'RoadUser1', 'RoadWidth', 'Rural', 'SpeedRel',
           'SurfaceType', 'TSD', 'UnitType', 'VehMov', 'VehVMC', 'VertFeature', 'Weather', 'CyclistInv', 'ArticVeh1',
           'RigidVeh', 'ArticVeh2', 'ContFactor']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Plot the summary box
myData.plot(kind='box', figsize=(15,15), subplots=True, layout=(4,5), sharex=False, sharey=False,
        color='orange', title = 'Driver Behaviour - Categorical - Box Summary', fontsize = 12)
plt.show()
