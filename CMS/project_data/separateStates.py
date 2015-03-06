import csv
import os.path
import time

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC','PR']
stateFiles = []
stateWriters = []
print len(states)

import time
timestr = time.strftime("%Y%m%d-%H%M%S")
print timestr


with open('Pharma_Doctor_Payment_data.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames

	subdirectory = timestr+'-states'
	try:
		os.mkdir(subdirectory)
	except Exception:
		pass

	for state in states:
		stateFiles.append(open(os.path.join(subdirectory, state+'.csv'),'wb'))

	for i in range(len(stateFiles)):
		stateWriters.append(csv.DictWriter(stateFiles[i], fieldnames=fieldnames))
		stateWriters[i].writeheader()	

	print states.index('FL')
	
	i=0
	for row in reader:
		try:
			stateWriters[states.index(row['Recipient_State'])].writerow(row)
		except Exception as e:
			print i
			#print e
			#print row
		i +=1
		#if(i%1000 == 0):
		#print i
		#print(str(i)+','+row['General_Transaction_ID'], row['Recipient_State'])
				


		
		