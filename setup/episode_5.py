from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"



print ()
print ("\t _____Search for 'New Zealand' in 245_____")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        if "New Zealand" in record['245'].value():
            print (record['245'])

print ()
print ("\t _____Search for 'New Zealand' in title_____")
print ()

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        if "New Zealand" in record.title():
            print (record['245'])
            print (record.title())
            print ()





print ()
print ("\t ___Building a basic parser!_____")
print ()


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print ("MMS ID:", record['001'].value())
        for my_field in record:
            #### Control fields (in the range 00x) don't have indicators. 
            #### We use this try/except catcher to allow us to elegantly handle both cases without encountering a breaking error, or a coding failure
            try:

                ind_1 = my_field.indicator1
                ind_2 = my_field.indicator2

                #### Setting an empty indicator to a more conventional and readable "/"
                if ind_1 == " ":
                    ind_1 = "/"
                if ind_2 == " ":
                    ind_2 = "/"

                print ("\tTag #:", my_field.tag, "Indicator 1:", ind_1 , "Indicator 2:", ind_2)
            except AttributeError:
                print ("\tTag #:", my_field.tag)

            for my_subfield_key, my_subfield_value in my_field:
                print ("\t\t", my_subfield_key, my_subfield_value)
            print ()
        print ()
        quit()