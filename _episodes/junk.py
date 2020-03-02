
import pymarc

my_marc_file = r"E:\GitHub\pymarc_basics\files\NLNZ_example_marc.mrc"

my_marc =  pymarc.MARCReader(open(my_marc_file, 'rb'), force_utf8=True)
for i, record in enumerate(my_marc):
    with open(f"{i}.json", "w", encoding='utf8') as data:
        data.write(record.as_json(indent=2))

