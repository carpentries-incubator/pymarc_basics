from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)

    for record in reader:
        for f in record.get_fields('035'):
            if "39818086" in f.value():
                print (record['001'].value())


        # quit()
    # for record in reader:
    #     print (record)
    #     break