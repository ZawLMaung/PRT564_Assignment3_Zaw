# Import libraries
from pandas import read_csv
from matplotlib import pyplot as plt

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingDriverBehaviourInliersData.csv'

# Define the data variable names
myNames = ['Experience', 'KlmsDist', 'Meter', 'Occupants', 'VehSeq', 'Airbag', 'AlcoholRel', 'LicClass', 'PedVMC',
           'HeavyVeh', 'Carriage', 'DUI', '4WD', 'Intername', 'LicStatus', 'NTRes', 'Community', 'Country', 'SafDevice', 'Sex']

# Read csv file
myData = read_csv(myFilename, names=myNames)

# print plot
myData.plot(kind='density', subplots=True, layout=(5,4), figsize=(15, 15), sharex=False,
            color='orange', title = 'Driver Behaviour - Density', fontsize = 12)
plt.show()