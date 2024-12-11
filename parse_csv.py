import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('new_names.csv', 'w') as new_file:
        fieldNames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')
        
        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)