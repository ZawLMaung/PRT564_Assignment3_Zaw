# Import libraries
import pandas as pd 
import numpy as np
from sklearn.feature_selection import chi2

# Define the data variable names
myNames = ['Mcycle', 'NbrTow', 'Airbag', 'VehVMC1', 'LicStatus', 'ABSSA3', 'Aboriginal', 'AgeBand', 'SafDevice',
           'Sex', 'State1', 'State2', 'RoadUser1', 'RoadWidth', 'TrafDensity', 'ATVInv', 'UnitType', 'VehDirTravel',
           'VehMov', 'VertFeature', 'RigidVeh', 'Businv', 'Pedestrian', 'InjuryDesc']

# Read dataset
myDataframe = pd.read_csv('TrainingRoadCrashInliersData.csv', names=myNames)

# Initialise a dataframe with 0 where the column names and index will be the same
myResult = pd.DataFrame(data=[(0 for i in range(len(myDataframe.columns))) for i in range(len(myDataframe.columns))], 
             columns=list(myDataframe.columns))
myResult.set_index(pd.Index(list(myDataframe.columns)), inplace = True)

# Find p_value for all columns and put them in the result matrix
for i in list(myDataframe.columns):
    for j in list(myDataframe.columns):
        if i != j:
            chi2_val, p_val = chi2(np.array(myDataframe[i]).reshape(-1, 1), np.array(myDataframe[j]).reshape(-1, 1))
            myResult.loc[i,j] = p_val

# Print correlation matrix
print()
print(myResult)
print()