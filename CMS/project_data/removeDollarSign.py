import csv
import os.path
import time

with open('Project_Data_with_ID.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = reader.fieldnames
	print fieldnames

	i=0
	with open('Project_Data_with_ID_no_dollar_sign.csv', 'wb') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()	
		for row in reader:
			try:
				row['Total_Amount_of_Payment_USDollars'] = row['Total_Amount_of_Payment_USDollars'][1:] 
				writer.writerow(row)
			except Exception as e:
				pass
				
			i +=1
			if(i%100000 == 0):
				print i
		