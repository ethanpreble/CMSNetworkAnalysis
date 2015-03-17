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


with open('Hosptial_ID.csv', 'rb') as csvfile:
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
	
	i=0
	for row in reader:
		try:
			stateWriters[states.index(row['Recipient_State'])].writerow(row)
			#stateWriters[states.index(row['Recipient_State'])].writerow(row['Physician_Profile_ID'],row['Total_Amount_of_Payment_USDollars'].replace("$",""))
		except Exception as e:
			pass
			#print i
			#print e
			#print row
		i +=1
		if(i%100000 == 0):
			print i
		#print(str(i)+','+row['General_Transaction_ID'], row['Recipient_State'])
				


#Physician_Profile_ID,Physician_Name,Recipient_Primary_Business_Address,Recipient_Zip_Code,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name,Total_Amount_of_Payment_USDollars,Nature_of_Payment_or_Transfer_of_Value
#27241,"Loc  Bao","4236 El Cajon Blvd  San Diego CA",92105,"Safco Dental Supply Co.",$128.00,"Gift"

		