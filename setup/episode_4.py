from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)

    for record in reader:
        if "eng" in record['008'].value():
            print (record['008'])


        # print (len(my_500s))


        # quit()
    # for record in reader:
    #     print (record)
    #     break