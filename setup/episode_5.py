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
print ("_______ Remove Field(s) with basic checks_______")
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

        break 


print ()
print ("_______ Remove Field(s) with logic_______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        my_fields = my_record.get_fields('035')
        for my_field in my_fields:
            if "ilsdb" in my_field.value():
                my_record.remove_field(my_field)


        print (len(record.get_fields('035')))
        print (len(my_record.get_fields('035')))

        break


print ()
print ("_______ Remove Subfield(s)_______")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        my_fields = my_record.get_fields('100')
        for my_field in my_fields:
            my_field.delete_subfield('d') 

        print (record['100'])
        print (my_record['100'])

        break


print ()
print ("_______ Add field _______")
print ()


from pymarc import Field 

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        ### making the new 245 field
        my_new_245_field = Field(

                            tag = '245', 

                            indicators = ['0','1'],

                            subfields = [
                                            'a', 'The pragmatic programmer : ',
                                            'b', 'from journeyman to master /',
                                            'c', 'Andrew Hunt, David Thomas.',
                                        ]
                            ) 
        ### adding the new field
        my_record.add_field(my_new_245_field)
        # my_record.add_ordered_field(my_new_245_field)

        ### showing the diffence
        for original_245 in record.get_fields('245'):
            print (original_245)
     
        print ("______")

        for my_record_245 in my_record.get_fields('245'):
            print (my_record_245)

        print (my_record)

        break 

print ()
print ("_______ making a new record _______")
print ()


from pymarc import Record

my_new_record = Record()

print (my_new_record)



print ()
print ("_______ making a new record populated_______")
print ()

from pymarc import Record

my_new_record = Record()
my_new_fields = []
my_new_fields.append(Field('003', data='Nz'))
my_new_fields.append(Field(tag='100', indicators=['1',''], subfields=['a','Gattuso, Jay,', 'd', 'd1978-']))
my_new_fields.append(Field(tag='245', indicators=['1','0'], subfields=['a','Goats. Are they the best animals? :', 'b', 'What about Cats!? /' ]))
my_new_fields.append(Field(tag='650', indicators=['','0'], subfields=['a','Goats', 'b', 'Competitive Pet Keeping']))
my_new_fields.append(Field(tag='650', indicators=['','0'], subfields=['a','Cats', 'b', 'Competitive Pet Keeping']))

for my_new_field in my_new_fields:
    my_new_record.add_ordered_field(my_new_field)

print (my_new_record)
