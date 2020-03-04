from pymarc import MARCReader
from copy import deepcopy

my_marc_file = "NLNZ_example_marc.marc"


a = ["Hello"]
# assigning b to be a
b = a
#printing b
print ("b =", b)
print (id(a))
print (id(b))
print ()

#changing a *only*!
a[0] = "World!"
#printing b
print ("b =", b)
print (id(a))
print (id(b))


print ()
print ("_______ making a deep copy _______")
print ()
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        print (id(record))
        print (id(my_record))

        print (my_record)

        break

print ()
print ("_______ making a deep copy _______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)

        # we only need to update the 'a' subfield.
        # note the catalogers punctuation... we must include the commas. 
        my_record['100']['a'] = "Manning, Arthuretta,"

        #comparing the two
        print (record['100'])
        print (my_record['100'])

        break

print ()
print ("_______ Remove Field(s)_______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)

        # We use the get_fields() method to generate a list of 300 get_fields
        # As there is only, we can just remove it. 
        for my_field in my_record.get_fields('300'):
            my_record.remove_field(my_field)

        #comparing the two
        print (record['300'])
        print (my_record['300'])

        break

print ()
print ("_______ Remove Field(s) with logic_______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)

        # We use the get_fields() method to generate a list of 300 get_fields
        my_fields = my_record.get_fields('300')
        
        # We test if this list of fields contains only one member
        if len(my_fields) == 1:
            print ("Only one 300 field found in record ID {}. Removing it.".format(record['001'].value()))
            for my_field in my_fields:
                my_record.remove_field(my_field)
        else:
            print ("More than one 300 field found in record ID {}. Doing nothing.".format(record['001'].value()))

        # comparing the two
        print ("Number of 300 fields in record:", len(record.get_fields('300')))
        print ("Number of 300 fields in my_record:", len(my_record.get_fields('300')))
        print()

        # testing the failing case 

                # We use the get_fields() method to generate a list of 300 get_fields
        my_fields = my_record.get_fields('035')
        
        # We test if this list of fields contains only one member
        if len(my_fields) == 1:
            print ("Only one 035 field found in record ID {}. Removing it.".format(record['001'].value()))
            for my_field in my_fields:
                my_record.remove_field(my_field)
        else:
            print ("More than one 035 field found in record ID {}. Doing nothing.".format(record['001'].value()))

        # comparing the two
        print ("Number of 035 fields in record:", len(record.get_fields('035')))
        print ("Number of 035 fields in my_record:", len(my_record.get_fields('035')))

        quit()