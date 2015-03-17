import csv
import os.path

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC','PR']

hospital_ID = set()
manufacterur_ID = set()
physician_ID = set()
#'Teaching_Hosptial_ID'
#'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID'
#'Physician_Profile_ID'


with open('Project_Data_with_ID_no_dollar_sign.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames
	
	i=0
	for row in reader:
		#try:
		hospital_ID.add(row['Teaching_Hospital_ID'])
		manufacterur_ID.add(row['Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID'])
		physician_ID.add(row['Physician_Profile_ID'])
		#print row['Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID']
	#	except Exception as e:
	#		pass
		i +=1
		if(i%200000 == 0):
			print i

			
			
			
print len(hospital_ID)
print len(manufacterur_ID)
print len(physician_ID)

#print totalByDocs
#print total


#f = open('TotalsByState_univ.txt', 'wb')
#for key in totalByUniv:
#	f.write(key+','+str(totalByUniv[key])+'\n')
#f.close()

#f = open('TotalsByState_doctor.txt', 'wb')
#for key in totalByDocs:
#	f.write(key+','+str(totalByDocs[key])+'\n')
#f.close()

#f = open('TotalsByState_total.txt', 'wb')
#for key in total:
#	f.write(key+','+str(total[key])+'\n')
#f.close()


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
		
		
