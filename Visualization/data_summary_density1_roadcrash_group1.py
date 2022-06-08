# Import libraries
from pandas import read_csv
from matplotlib import pyplot as plt

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Print plot
myData.plot(kind='density', subplots=True, layout=(3,4), figsize=(15, 15), sharex=False,
            color='blue', title = 'Road Crash - Density', fontsize = 12)
plt.show()