from pymarc import MARCReader

my_marc_file = "NLNZ_example_marc.marc"

### We'll add records to this list. It can have a membership of 1 
my_marc_records = []
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        ### we add out records to our list of records
        my_marc_records.append(record)
        ### and print the IDs so we can see whats happening
        print (record['001'])

# we create a new file
my_new_marc_filename = "my_new_marc_file.marc" 
with open(my_new_marc_filename , 'wb') as data:
    for my_record in my_marc_records:
        ### and write each record to it
        data.write(my_record.as_marc())

print ()
print ("___")
print ()

### we open the new marc file
with open(my_new_marc_filename, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        ### and print the IDs so we can validate we save all the records
        print (record['001'])


print ()
print ("______ Basic saver ______")
print ()


my_new_marc_filename = "my_new_marc_file.marc" 
with open(my_new_marc_filename , 'wb') as data:
    for my_record in my_marc_records:
        data.write(my_record.as_marc())