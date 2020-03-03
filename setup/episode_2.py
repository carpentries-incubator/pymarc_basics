from pymarc import MARCReader

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record)
        quit()

