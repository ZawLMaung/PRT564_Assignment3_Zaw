# Input libraries
from matplotlib import pyplot as plt
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'TrainingRoadCrashInliersData.csv'

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Plot the summary box
myData.plot(kind='box', figsize=(15,15), subplots=True, layout=(2,6), sharex=False, sharey=False,
        color='blue', title = 'Road Crash - Categorical - Box Summary', fontsize = 12)
plt.show()