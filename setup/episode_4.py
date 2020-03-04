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


        ind_2 =  record['245'].indicator2
        if ind_2 != '0':
            print (record['245'])
            print ()
#         my_record = deepcopy(record)
#         print (id(record))
#         print (id(my_record))

#         print (my_record)

#         break

# print ()
# print ("_______ making a deep copy _______")
# print ()

# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         my_record = deepcopy(record)

#         # we only need to update the 'a' subfield.
#         # note the catalogers punctuation... we must include the commas. 
#         my_record['100']['a'] = "Manning, Arthuretta,"

#         #comparing the two
#         print (my_record['100'])
#         print (record['100'])

#         break



