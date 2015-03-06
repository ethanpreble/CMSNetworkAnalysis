import csv
import os.path
import time

states = {'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'}
stateFiles = []
print len(states)

import time
timestr = time.strftime("%Y%m%d-%H%M%S")
print timestr

subdirectory = timestr+'-states'
try:
    os.mkdir(subdirectory)
except Exception:
    pass

for state in states:
	stateFiles.append(open(os.path.join(subdirectory, state+'.csv'),'w'))


with open('Pharma_Doctor_Payment_data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldNames = reader.fieldnames
	print fieldNames
	#for row in reader:
	#	print(row['General_Transaction_ID'], row['Recipient_State'])
		
		
		
		