import csv

fields = ['empid','empname','empaddress']
rows =[['100','eric','Scottsdale'],
        ['200','claire','Glendale']]

with open('employee.csv','w',newline='') as csvfile:
    empwriter = csv.writer(csvfile)
    empwriter.writerow(fields)
    empwriter.writerows(rows)