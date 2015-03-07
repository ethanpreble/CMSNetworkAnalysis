import csv
import os.path
import time

with open('Pharma_Doctor_Payment_data.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames

	i=0
	with open('no_ID.csv', 'wb') as no_ID_file:
		with open('yes_ID.csv', 'wb') as yes_ID_file:
			writer_no = csv.DictWriter(no_ID_file, fieldnames=fieldnames)
			writer_yes = csv.DictWriter(yes_ID_file, fieldnames=fieldnames)
			writer_no.writeheader()
			writer_yes.writeheader()		
			
			for row in reader:
				try:
					if(row['Physician_Profile_ID']==''):
						writer_no.writerow(row)
					else:
						writer_yes.writerow(row)
				except Exception as e:
					pass
					
				i +=1
				if(i%100000 == 0):
					print i
			