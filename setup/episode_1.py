import sys
import pymarc

print(sys.executable)

print ("{}".format("Hello! World!"))

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
    reader = pymarc.MARCReader(data)
    for record in reader:
        print (record.title())

