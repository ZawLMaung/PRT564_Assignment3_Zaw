# Import libraries
from pandas import read_csv

# Load the csv file using read_csv function of pandas library
myFilename = 'AllVariablesTrainingDriverBehaviourData.csv'

# Define the data variable names
myNames = ['Experience', 'KlmsDist', 'Mcycle', 'Meter', 'NbrInj', 'NbrTow', 'Occupants', 'VehSeq', 'AccDay', 'AccDesc',
          'AccTime', 'Acc10y', 'AccYear', 'Airbag', 'AlcoholRel', 'Circum1', 'Damage', 'Defects', 'LicClass', 'PedVMC',
          'Tow', 'TrafficControl', 'VehVMC1', 'VehVMC2','StreetFilter', 'Cyclist','Veh1TravelDir', 'DistPersons',
          'HeavyVeh', 'AccMonth', 'Carriage', 'Circum2', 'Accident', 'DirIDMark','DistanceID', 'DrugRel', 'AccVal',
          'DUI', '4WD', 'GeoCoded', 'Inspected', 'InsuInfo', 'TowAway','VehFire', 'Vetted', 'HitRun', 'HorFeature',
          'InjCode', 'InterName', 'LicStatus', 'LightCond', 'MinInjCode', 'MinInjDesc', 'Municipality', 'NTRes',
          'ABSSA3', 'LGA', 'NearID', 'NbrUnits', 'NbrRecords', 'OZTBefAft', 'OthFeature', 'Aboriginal', 'Ejected',
          'AgeBand', 'Age', 'Community', 'Country', 'SafDevice', 'Sex', 'State1', 'State2', 'PoliceArea',
          'PoliceDistrict', 'PoliceSup', 'RUMDesc', 'RegoExp', 'RegoState', 'RoadDivision', 'MainStFilter', 'RoadName',
          'RoadUser1', 'RoadUser2', 'RoadWidth', 'RdUserCode', 'Rural', 'SpeedLimit', 'SpeedRel', 'Sub/Area',
          'SurfaceType', 'TSD', 'TrafDensity', 'UnitMake', 'UnitModel', 'ATVInv', 'UnitTypeCode', 'UnitType',
          'UnitYear', 'VehDirTravel', 'VehMov', 'VehVMC', 'VertFeature', 'Weather', 'AccMthName', 'DistNbrCrash',
          'DARunTotal', 'CyclistInv', 'ArticVeh1', 'RigidVeh', 'BusInv', 'InterceptFilter', 'PointFound', 'ArticVeh2',
          'Veh6TravelDir', 'Veh5TravelDir', 'Veh4TravelDir', 'Veh2TravelDir', 'Veh3TravelDir', 'Pedestrian',
          'ContFactor']

# Read the csv file
myData = read_csv(myFilename, names=myNames)

# Print a quick preview of first 5 rows
myPeek = myData.head(5)
print()
print(myPeek)
print()