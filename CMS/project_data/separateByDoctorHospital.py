import csv
import os.path
import time

with open('Project_Data_with_ID_no_dollar_sign.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames

	
	with open('Hosptial_ID.csv', 'wb') as Hospital_ID_file:
		with open('Physician_ID.csv', 'wb') as Physician_ID_file:
			writer_Hospital = csv.DictWriter(Hospital_ID_file, fieldnames=fieldnames)
			writer_Physician = csv.DictWriter(Physician_ID_file, fieldnames=fieldnames)
			writer_Hospital.writeheader()
			writer_Physician.writeheader()		
			
			i=0
			for row in reader:
				try:
					if(row['Physician_Profile_ID']!=''):
						writer_Physician.writerow(row)
					if(row['Teaching_Hospital_ID']!=''):
						writer_Hospital.writerow(row)
				except Exception as e:
					pass
					
				i +=1
				if(i%100000 == 0):
					print i
			