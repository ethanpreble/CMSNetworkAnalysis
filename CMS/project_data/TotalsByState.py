import csv
import os.path

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC','PR']

totalByUniv = {}
totalByDocs = {}
total={}

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

with open('Pharma_Doctor_Payment_data_no_dollar_sign.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames
	
	i=0
	for row in reader:
		try:
			if(row['Physician_Profile_ID']==''):
				totalByUniv[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
			else:
				totalByDocs[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
			total[row['Recipient_State']] += float(row['Total_Amount_of_Payment_USDollars'])
		except Exception as e:
			pass
		i +=1
		if(i%200000 == 0):
			print i

			
			
			
print totalByUniv
print totalByDocs
print total


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
		
		
		
