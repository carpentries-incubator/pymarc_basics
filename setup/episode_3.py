from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


print ("Finding specific fields with PyMARC")
print ()
print ("\t ______Print a record______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record)
        break

print ()
print ("\t ______Print a field______")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record['245'])

print ()
print ("\t ______Print a key that doesn't exist______")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record['this_key_doesnt_exist'])
        break


print()
print ("\t ______Accessing Subfields______")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print ("Subfield 'a':", record['245']['a'])
        print ("Subfield 'b':", record['245']['b'])
        print ("Subfield 'c':", record['245']['c'])
        break

print()
print ("\t ______Print the same information in different ways______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (type(record))
        print ()
        print (record['245'])
        print (type(record['245']))
        print ()
        print (record['245'].value())
        print (type(record['245'].value()))
        print ()
        print (record['245']['a'])
        print (type(record['245']['a']))
        print ()
        print (record.title())
        print (type(record.title()))
        break

# print ()
print ("\t ______Find a particular record by its unique ID_____")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        if record['001'].value() == str(99628153502836):
            print ("Success! found record with id 99628153502836")



print ()
print ("\t ______Find a particular record by its unique ID as a variable_____")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    search_id = 99628153502836
    for record in reader:
        if record['001'].value() == str(search_id):
            print (f"Success! found record with id {search_id}")