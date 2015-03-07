import csv
import os.path
import time

with open('Pharma_Doctor_Payment_data.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames

	with open('Pharma_Doctor_Payment_data_no_dollar_sign.csv', 'wb') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()	
		for row in reader:
			try:
				newRow = []
				for fieldname in fieldnames:
					if fieldname != 'Total_Amount_of_Payment_USDollars':
						newRow.append({'fieldname':row[fieldname]})
					else:
						newRow.append({'fieldname':row[fieldname][1:]})
				#print row['Total_Amount_of_Payment_USDollars']
				#dollars = row['Total_Amount_of_Payment_USDollars']
				#dollars = dollars[1:]
				#writer.writerow({'Total_Amount_of_Payment_USDollars':dollars})
				write.writerow(newRow)
			except Exception as e:
				pass
		
		#			stateWriters[states.index(row['Recipient_State'])].writerow(row['Physician_Profile_ID'],row['Total_Amount_of_Payment_USDollars'].replace("$",""))
		#    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

