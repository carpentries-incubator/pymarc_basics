from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


# print ("Finding specific fields with PyMARC")
# print ()
# print ("\t ______Print a record______")
# print ()

# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         print (record)
#         break

# print ()
# print ("\t ______Print a field______")
# print ()
# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         print (record['245'])

# print ()
# print ("\t ______Print a key that doesn't exist______")
# print ()
# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         print (record['this_key_doesnt_exist'])
#         break


# print()
# print ("\t ______Accessing Subfields______")
# print ()
# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         print ("Subfield 'a':", record['245']['a'])
#         print ("Subfield 'b':", record['245']['b'])
#         print ("Subfield 'c':", record['245']['c'])
#         break

# print()
# print ("\t ______Print the same information in different ways______")
# print ()

# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         print (type(record))
#         print ()
#         print (record['245'])
#         print (type(record['245']))
#         print ()
#         print (record['245'].value())
#         print (type(record['245'].value()))
#         print ()
#         print (record['245']['a'])
#         print (type(record['245']['a']))
#         print ()
#         print (record.title())
#         print (type(record.title()))
#         break

# print ()
# print ("\t ______Find a particular record by its unique ID_____")
# print ()
# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         if record['001'].value() == str(99628153502836):
#             print ("Success! found record with id 99628153502836")



# print ()
# print ("\t ______Find a particular record by its unique ID as a variable_____")
# print ()
# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     search_id = 99628153502836
#     for record in reader:
#         if record['001'].value() == str(search_id):
#             print (f"Success! found record with id {search_id}")



# print ()
# print ("\t _____Search for 'New Zealand' in 245_____")
# print ()

# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         if "New Zealand" in record['245'].value():
#             print (record['245'])

# print ()
# print ("\t _____Search for 'New Zealand' in title_____")
# print ()

# with open(my_marc_file, 'rb') as data:
#     reader = MARCReader(data)
#     for record in reader:
#         if "New Zealand" in record.title():
#             print (record['245'])
#             print (record.title())
#             print ()





# print ()
# print ("\t ___Building a basic parser!_____")
# print ()


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        # print ("MMS ID:", record['001'].value())
        # for my_field in record:
        #     #### Control fields (in the range 00x) don't have indicators. 
        #     #### We use this try/except catcher to allow us to elegantly handle both cases without encountering a breaking error, or a coding failure
        #     try:

        #         ind_1 = my_field.indicator1
        #         ind_2 = my_field.indicator2

        #         #### Setting an empty indicator to a more conventional and readable "/"
        #         if ind_1 == " ":
        #             ind_1 = "/"
        #         if ind_2 == " ":
        #             ind_2 = "/"

        #         print ("\tTag #:", my_field.tag, "Indicator 1:", ind_1 , "Indicator 2:", ind_2)
        #     except AttributeError:
        #         print ("\tTag #:", my_field.tag)

        #     for my_subfield_key, my_subfield_value in my_field:
        #         print ("\t\t", my_subfield_key, my_subfield_value)
        #     print ()
        # print ()
        # quit()

        print (record.author())
        print (record.isbn())
        print (record.issn())
        print (record.issn_title())
        print (record.leader) 
        print (record.location())
        print (record.pos)
        print (record.publisher())
        print (record.pubyear())
        print (record.series())
        print (record.sudoc())
        print (record.title())
        print (record.uniformtitle())
        print ([x.value() for x in record.notes()])
        print ([x.value() for x in record.subjects()])
        print ([x.value() for x in record.physicaldescription()])

        quit()