---
title: "Parsing with pymarc"
teaching: 0
exercises: 0
objectives:
- How to read a marc record with pymarc
- Finding specific fields with pymarc
- finding specific data with pymarc
---
Episode 3: Parsing with pymarc

Start a new file in your IDE <code>episode_3.py</code>

Set up the basic record reader like we did in episode 2:

	import pymarc

	my_marc_file = "NLNZ_example_marc.mrc"

	reader = pymarc.MARCReader(file(my_marc_file)) 

	for record in reader:
		print (record)


We can used the data object created by pymarc to only process fields we're interested in. We can do that by telling python the field name e.g. <code>print (record['245'])</code> In this piece of code we're asking pymarc to print any field in our record object that has the label, or index, <code>245</code>  

If we add this little piece of code to our basic file parser we can see all the title statements for our test set:


	for record in reader:
		print (record['245'])

 _____

	=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
	=245  10$aDifficult country :$ban informal history of Murchison /$cMargaret C. Brown.
	=245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
	=245  10$aAs high as the hills :$bthe centennial history of Picton /$cby Henry D. Kelly.
	=245  10$aRevised establishment plan.
	=245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.
	=245  10$aChilton Saint James :$ba celebration of 75 years, 1918-1993 /$cJocelyn Kerslake.
	=245  10$aTatum, a celebration :$b50 years of Tatum Park /$cby Tom Howarth.
	=245  04$aThe Discussion document of the Working Party on Fire Service Levy /$b... prepared by the Working Party on the Fire Service Levy.
	=245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.

We can use the same index method to get to the subfields:

	for record in reader:
		print (record['245']['a'])

_____

	Larger than life :
	Difficult country :
	These fortunate isles :
	As high as the hills :
	Revised establishment plan.
	A Statistical profile of young women /
	Chilton Saint James :
	Tatum, a celebration :
	The Discussion document of the Working Party on Fire Service Levy /
	1991 New Zealand census of population and dwellings.

What do you notice about these pieces of data? 

There are a few other ways we can get to the same data that are worth exploring. 

The data object that pymarc creates has a method called "<code>value()</code>". We can use this to process the data field and return a text string without any subfield markers. 

This is also a good opportunity to axplore another useful method, "<code>type()</code>". Lets have a look a one record:

	for record in reader:
		print (type(record))
		print ()
		print (record['245'].value())
		print (type(record['245'].value()))
		print ()
		print (record['245'])
		print (type(record['245'])
		print ()
		print (record['245']['a'])
		print (type(record['245']['a']))
		quit()
_____

	<class 'pymarc.record.Record'>

	Larger than life : the story of Eric Baume / by Arthur Manning.
	<class 'str'>

	=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
	<class 'pymarc.field.Field'>

	Larger than life :
	<class 'str'>


We can use a simliar approach tp find a particular record. Lets say we're looking for the record with the 001 identifer of <code>99628153502836</code>. We can loop through the records in our <code>pymarc.reader</code> object and look for a match:

 	for record in reader:
 		if record['001'].value == str(99628153502836):
 			print ("Success! found record with id 99628153502836")

We can make this a little more useful by abstracting the search id into a variable:

	search_id = 99628153502836
	for record in reader:
		if record['001'].value() == str(search_id):
			print (f"Success! found record with id {search_id}")

What are the main differences between these two code snippets?

Why do we need the <code>str()</code> conversion? Can you think of a different way of solving the same problem?

Lets make our search a little more interesting. Lets say we're interested in in any record that contains the string "New Zealand" in the <code>245</code> field

    if "New Zealand" in record['245'].value():
        print (record['245'])
_____
	=245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
	=245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.
	=245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.

What about if we want any record that contains the string "New Zealand"? How might we adapt the code? 

	if "New Zealand" in str(record):
		print (record) 
		print()

This could result in an overwhleming amount of data... give it a go and think about how you might frame that question in a way that helps to refine the data into a useful form. 

Lets refine the question, and ask to see any MARC field that contains our search string. We can do this by adding another loop. We also might want to think about how we assocate each match with a particular record. One way of doing this would be to print the reocrd ID as well as the matching field:

    if "New Zealand" in str(record):
        for field in record:
            if "New Zealand" in field.value():
                print (record['001'].value(), field)  

        print ()

____

	9962783502836 =500  \\$aEric Baume was a New Zealander.
	9962783502836 =650  \0$aAuthors, New Zealand$y20th century$xBiography.

	99627923502836 =245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
	99627923502836 =651  \0$aNew Zealand$xForeign public opinion, Russian$xHistory.

	99628063502836 =650  \0$aElectric power distribution$zNew Zealand$zBay of Plenty (Region)$xDeregulation.
	99628063502836 =650  \0$aElectric utilities$zNew Zealand$zBay of Plenty (Region)$xDeregulation.
	99628063502836 =650  \0$aPrivatization$zNew Zealand$zBay of Plenty (Region)

	99628093502836 =245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.
	99628093502836 =650  \0$aYoung women$zNew Zealand$xStatistics.
	99628093502836 =710  20$aYWCA of Aotearoa New Zealand.
	99628093502836 =710  20$aShell Group of Companies in New Zealand.

	99628113502836 =650  \0$aChurch schools$zNew Zealand$zLower Hutt$xHistory.
	99628113502836 =650  \0$aSingle-sex schools$zNew Zealand$zLower Hutt$xHistory.

	99628123502836 =260  0\$a[Wellington, N.Z.] :$bScout Association of New Zealand,$c1992.
	99628123502836 =650  \0$aBoy Scouts$zNew Zealand$xHistory.
	99628123502836 =710  20$aScout Association of New Zealand.

	99628153502836 =610  20$aNew Zealand Fire Service Commission$xFinance.
	99628153502836 =650  \0$aFire departments$zNew Zealand$xFinance.
	99628153502836 =710  10$aNew Zealand.$bDepartment of Internal Affairs.
	99628153502836 =710  10$aNew Zealand.$bWorking Party on the Fire Service Levy.

	99628163502836 =245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.
	99628163502836 =500  \\$a"New Zealanders' living arrangements, including their household composition and family type characteristics are the focus of this report. Information on private dwellings is also included"--Back cover.
	99628163502836 =500  \\$aCover title: 1991 census of population and dwellings : New Zealanders at home.
	99628163502836 =500  \\$aSpine title: Census 1991 : New Zealanders at home.
	99628163502836 =650  \0$aHouseholds$zNew Zealand$xStatistics.
	99628163502836 =650  \0$aFamilies$zNew Zealand$xStatistics.
	99628163502836 =650  \0$aCost and standard of living$zNew Zealand$xStatistics.
	99628163502836 =651  \0$aNew Zealand$xCensus, 1991.
	99628163502836 =651  \0$aNew Zealand$xPopulation$xStatistics.
	99628163502836 =710  10$aNew Zealand.$bDepartment of Statistics.
	99628163502836 =740  01$a1991 census of population and dwellings, New Zealanders at home.
	99628163502836 =740  01$aCensus 1991, New Zealanders at home.
	99628163502836 =740  01$aNew Zealanders at home.


Experiments! 

See if you can find any records with the OCLC identifer 39818086
Can you count how many records have more than one 500 fields?
#todo - what is the main language indicator!?
Can you find out how many records describe an item thats written in English? (hint: We can look in the <code>record.leader</code> in position )
