import pymarc

my_marc =  pymarc.MARCReader(open(r"E:\work\NATBIB questions\marc_data/pubsnzmetadatajanuary2020_cleaned.mrc", 'rb'), force_utf8=True)

new_marc = []
for i, r in enumerate(my_marc):
    new_marc.append(r)
    
    if i == 1000:
        break

with open('NLNZ_1000_example_marc.mrc', 'wb') as out:
    for record in new_marc:
        out.write(record.as_marc())



my_marc =  pymarc.MARCReader(open(r"NLNZ_1000_example_marc.mrc", 'rb'), force_utf8=True)
for i, r in enumerate(my_marc):
    print (r['001'])
