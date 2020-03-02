import pymarc

my_marc_file = r"E:\GitHub\pymarc_basics\files\NLNZ_example_marc.mrc"

reader =  pymarc.MARCReader(open(my_marc_file, 'rb'), force_utf8=True)

search_id = 99628153502836

subfield_codes_for_245 = 'a', 'b', 'c', 'f', 'g', 'h', 'k', 'n', 'p', 's', '6', '8'

for record in reader:
    # print (str(record))
    # print (type(record))
    # print ()
    # print (record['245'].value())
    # print (type(record['245'].value()))
    # print ()
    # print (record['245'])
    # print (type(record['245']))
    # print ()
    # print (record['245']['a'])
    # print (type(record['245']['a']))
    # quit()


    # if record['001'].value() == str(search_id):
        # print (f"Success! found record with id {search_id}")

    # if "New Zealand" in str(record):
    #         if "New Zealand" in field.value():
    #             print (record['001'].value(), field)
    #     print ()
    # for field in record:
# for record in reader:
# for record in reader:
# for record in reader:
    ind_2 =  record['245'].indicator2
    if ind_2 != '0':
        print (record['245'])
        print ()