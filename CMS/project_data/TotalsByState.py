import csv
import os.path

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC','PR']

totalByUniv = {}
totalByDocs = {}
total={}
totalUS=0.0
totalDocs=0.0
totalHospital=0.0

hospitalSets = {}
physicianSets = {}

for s in states:
	hospitalSets[s] = set()
	physicianSets[s] = set()

for s in states:
	totalByUniv[s]=0
	totalByDocs[s]=0
	total[s]=0
	
#for key in total:
#	print key
#	print total[key]
	
#print totalByUniv
#print totalByDocs

#print totalByUniv['AL']
#totalByUniv['fake'] += totalByUniv['fake']
#print totalByUniv['fake']

with open('Project_Data_with_ID_no_dollar_sign.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames
	
	i=0
	for row in reader:
		try:
			#if(row['Physician_Profile_ID']==''):
			#	totalByUniv[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
			#else:
			#	totalByDocs[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
			if(row['Physician_Profile_ID']!=''):
				totalByDocs[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
				totalDocs+=float(row['Total_Amount_of_Payment_USDollars'])
			if(row['Teaching_Hospital_ID']!=''):
				totalByUniv[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])	
				totalHospital+=float(row['Total_Amount_of_Payment_USDollars'])
			total[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
			totalUS+=float(row['Total_Amount_of_Payment_USDollars'])
		
			hospitalSets[row['Recipient_State']].add(row['Teaching_Hospital_ID'])
			physicianSets[row['Recipient_State']].add(row['Physician_Profile_ID'])

			
			
		except Exception as e:
			pass
		i +=1
		if(i%200000 == 0):
			print i

			
			
			
#print totalByUniv
#print totalByDocs
#print total
print totalUS
print totalDocs
print totalHospital


f = open('TotalsByState_univ.txt', 'wb')
for key in totalByUniv:
	f.write(key+','+str(totalByUniv[key])+'\n')
f.close()

f = open('TotalsByState_doctor.txt', 'wb')
for key in totalByDocs:
	f.write(key+','+str(totalByDocs[key])+'\n')
f.close()

f = open('TotalsByState_total.txt', 'wb')
for key in total:
	f.write(key+','+str(total[key])+'\n')
f.close()

f = open('TotalHospitalOverNumHospitalsByState.txt', 'wb')
for key in totalByUniv:
	val = totalByUniv[key]/len(hospitalSets[key])
	f.write(key+','+str(val)+'\n')
f.close()

f = open('TotalPhysicianOverNumPhysiciansByState.txt', 'wb')
for key in totalByDocs:
	val = totalByDocs[key]/len(physicianSets[key])
	f.write(key+','+str(val)+'\n')
f.close()


for key in hospitalSets:
	print len(hospitalSets[key])
print "\n"
for key in physicianSets:
	print len(physicianSets[key])

#with open('TotalsByState_univ.csv', 'wb') as f1:
#	with open('TotalsByState_doc.csv', 'wb') as f2:
#		with open('TotalsByState_total.csv', 'wb') as f3:
#			writer1 = csv.DictWriter(f1, ['state','total'])
#			writer2 = csv.DictWriter(f2, ['state','total'])
#			writer3 = csv.DictWriter(f3, ['state','total'])
#			writer1.writeheader()
#			writer2.writeheader()
#			writer3.writeheader()
			
#			for key in totalByUniv:
#				writer1.writerow([key,str(totalByUniv[key])])
#			for key in totalByDocs:
#				writer2.writerow([key,str(totalByDocs[key])])
#			for key in total:
#				writer3.writerow([key,str(total[key])])
		
		#with open('names.csv', 'w') as csvfile:
   # fieldnames = ['first_name', 'last_name']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'}
		
		
