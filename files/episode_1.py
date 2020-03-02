import pymarc

my_marc_file = "NLNZ_example_marc.marc"

reader = pymarc.MARCReader(open(my_marc_file, 'rb'), force_utf8="True") 

for record in reader:
    print (record['245'])