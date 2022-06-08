# Input libraries
from matplotlib import pyplot as plt
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingDriverBehaviourInliersData.csv'

# Define the data variable names
myNames = ['Experience', 'KlmsDist', 'Meter', 'Occupants', 'VehSeq', 'Airbag', 'AlcoholRel', 'LicClass', 'PedVMC',
           'HeavyVeh', 'Carriage', 'DUI', '4WD', 'Intername', 'LicStatus', 'NTRes', 'Community', 'Country', 'SafDevice', 'Sex']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Plot the summary box
myData.plot(kind='box', figsize=(15,15), subplots=True, layout=(4,5), sharex=False, sharey=False,
        color='orange', title = 'Driver Behaviour - Box Summary', fontsize = 12)
plt.show()
