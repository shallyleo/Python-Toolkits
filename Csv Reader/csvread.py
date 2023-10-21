import csv

with open('file_name.csv', 'r') as file:
    reader = csv.reader(file)
    email_list = []
    for row in reader:
        email_list.append(row[2])

with open('emails.txt', 'w') as file:
    for email in email_list:
        file.write(email + ', \n')

file.close()
