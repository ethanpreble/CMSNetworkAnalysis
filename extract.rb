#!/usr/bin/env ruby

require 'csv'

f = File.open('payments.csv')
fw = File.open('extracted.csv', 'w')
header = 'Physician_Profile_ID' + "," + 'Physician_First_Name' + "," + 'Physician_Middle_Name' + "," + 'Physician_Last_Name' + "," + 
	'Recipient_Primary_Business_Street_Address_Line1' + "," + 'Recipient_Primary_Business_Street_Address_Line2' + "," + 'Recipient_City' + "," + 
	'Recipient_State' + "," + 'Recipient_Zip_Code' + "," + 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name' + "," + 'Total_Amount_of_Payment_USDollars' + "," + 'Nature_of_Payment_or_Transfer_of_Value'
fw.puts(header)
CSV.foreach(f, headers:true) do |r|
	line = r['Physician_Profile_ID'].to_s + "," + r['Physician_First_Name'].to_s + "," + r['Physician_Middle_Name'].to_s + "," + r['Physician_Last_Name'].to_s + ",\"" + 
	r['Recipient_Primary_Business_Street_Address_Line1'].to_s + "\",\"" + r['Recipient_Primary_Business_Street_Address_Line2'].to_s + "\"," + r['Recipient_City'].to_s + "," + 
	r['Recipient_State'].to_s + "," + r['Recipient_Zip_Code'].to_s + ",\"" + r['Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name'].to_s + "\"," + r['Total_Amount_of_Payment_USDollars'].to_s + ",\"" + r['Nature_of_Payment_or_Transfer_of_Value'].to_s + "\""
	fw.puts(line)
end

f.close	
fw.close

