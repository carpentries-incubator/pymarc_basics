---
title: Parsing with pymarc
teaching: 30
exercises: 30
objectives:
- How to read a marc record with pymarc
- Finding specific fields with pymarc
- finding specific data with pymarc
---
## Episode 3: Parsing with pymarc

# Finding specific fields with PyMARC

Start a new file in your IDE <code>episode_3.py</code>

Set up the basic record reader like we did in episode 2:


```Python
from pymarc import MARCReader

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record)
```

We can used the data object created by pymarc to only process fields we're interested in. We can do that by telling python the field name e.g. <code>print (record['245'])</code> In this piece of code we're asking pymarc to print any field in our record object that has the label/name <code>245</code>  

If we add this piece of code to our basic file parser we can see all the title statements for our test set:

```Python
for record in reader:
	print (record['245'])
```
 _____

```
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
```

What is the data type does the record object look like? (<code>print (type(record)) won't help much, can you think why?</code>) 

Behind the scenes when this script is run, python looks at the date object that pymarc created, and looks for the bit that has the label, or 'key' of "245". 

See what happens if you give it a key that isn't included in the data object:


```Python
for record in reader:
	print (record['this_key_doesnt_exist'])
	quit()
```
___
```
None

```

Notice it doesn't give you an error or otherwise let you know it did find that key in the data object. Its useful to know this happens if we use an key that doesn't exist. If you see the return <code>None</code> in your scripts where you are expecting an actual value, double check the key you've used. Common errors would be typos (e.g. <code>record['254']</code> instead of <code>record['245']</code>) or using a number instead of a string (e.g. <code>record[245]</code> instead of <code>record['245']</code>).

In this case, returns <code>None</code>, which itself is an important concept in Python. Its worth pausing for a moment and making sure we understand what <code>None</code> means in the Python context. 

>The None keyword is used to define a null value, or no value at all.
>
>None is not the same as 0, False, or an empty string. 
>
>None is a datatype of its own (NoneType) and only None can be None."

https://www.w3schools.com/python/ref_keyword_none.asp 

# Accessing Subfields

We can use the same 'key' method to get to any subfields we might have:

```Python
for record in reader:
	print ("Subfield 'a':", record['245']['a'])
	print ("Subfield 'b':", record['245']['b'])
	print ("Subfield 'c':", record['245']['c'])
	quit()
```
_____

```
Subfield 'a': Larger than life :
Subfield 'b': the story of Eric Baume /
Subfield 'c': by Arthur Manning.
```
What do you notice about these pieces of data? Whatg might we need to consider if we want to use data that potentially spans multiple subfields? 

There are a few other ways we can get to the same data that are worth exploring. 

The data object that pymarc creates has a method called "<code>value()</code>". We can use this to return the data field as text string without any subfield markers or indicators. 

This is also a good opportunity to explore another useful method, "<code>type()</code>". 

PyMARC gives us some convenient keywords to help us access key bits of data. One of those is the keyword <code>.title()</code>. 

Lets have a look a one record and what these various methods produce:

```Python
for record in reader:
    print (type(record))
    print ()
    print (record['245'])
    print (type(record['245']))
    print ()
    print (record['245'].value())
    print (type(record['245'].value()))
    print ()
    print (record['245']['a'])
    print (type(record['245']['a']))
    print ()
    print (record.title())
    print (type(record.title()))
    quit()
```
_____

```
<class 'pymarc.record.Record'>

=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
<class 'pymarc.field.Field'>

Larger than life : the story of Eric Baume / by Arthur Manning.
<class 'str'>

Larger than life :
<class 'str'>

Larger than life : the story of Eric Baume /
<class 'str'>
```

We can use a similar approach to find a particular record. Lets say we're looking for the record with the 001 identifer of <code>99628153502836</code>. We can loop through the records in our <code>pymarc.reader</code> object and look for a match:

```Python
	for record in reader:
		if record['001'].value() == str(99628153502836):
			print ("Success! found record with id 99628153502836")
```

We can make this a little more useful by abstracting the search id into a variable:

```Python
	search_id = 99628153502836
	for record in reader:
		if record['001'].value() == str(search_id):
			print (f"Success! found record with id {search_id}")
```

What are the main differences between these two code snippets?

Why do we need the <code>str()</code> conversion? Can you think of a different way of solving the same problem?

Lets make our search a little more interesting. Lets say we're interested in in any record that contains the string "New Zealand" in the <code>245</code> field

```Python
    if "New Zealand" in record['245'].value():
        print (record['245'])
```
_____
```
	=245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
	=245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.
	=245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.
```

Lets have a look at what happens if we use the <code>.title()</code> method as our string that we're searching:

```Python
for record in reader:
    if "New Zealand" in record.title():
        print (record['245'])
        print (record.title())
        print ()
```
___
```
=245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
These fortunate isles : some Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /

=245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.
1991 New Zealand census of population and dwellings.
````
Notice this difference between these two scripts. This is a really good example of a paradigm we find in coding, explicit vs implicit. 

>In programming, implicit is often used to refer to something that’s done for you by other code behind the scenes. 
>Explicit is the manual approach to accomplishing the change you wish to have by writing out the instructions to be done explicitly.

https://blog.codeship.com/what-is-the-difference-between-implicit-vs-explicit-programming/

In this case, the programmers behind the pymarc library have made some choices about which version of a title they think is the most straightforward. This is based on what the MARC standard says about a title, and how to interpret the field as a human being. 
We don't necessarily know what those choices where, we simply trust that they made sensible one! This is an example of implicit coding. If we built our title parser, that read the field, and its associated subfields, and used some logic to turn that data into a single string like <code>record.title()</code> does, we would be explicitly coding this solution. 

____ 

What about if we want any record that contains the string "New Zealand"? How might we adapt the code? 

```Python
	if "New Zealand" in str(record):
		print (record) 
		print()
```

This could result in an overwhelming amount of data if we're not careful. Lets have a think about how we might frame that question in a way that helps to refine the data into a useful form. 

What happens if we  ask to see any MARC field that contains our search string. We can do this by adding another loop. 
We also might want to think about how we associate each match with a particular record. One way of doing this would be to print the record ID as well as the matching field:

```Python
    if "New Zealand" in str(record):
        for field in record:
            if "New Zealand" in field.value():
                print (record['001'].value(), field)  
        print ()
```
____

```
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
```

We can use the same loop/iterator approach to process any field that has subfields. Lets see what that looks likes:

```Python
	for record in reader:
		for field in record:
			for subfield in field:
				print (subfield)
		quit()
```
____
```
('z', '4260')
('a', '(nzNZBN)687856')
('9', '   67095940')
('a', '(Nz)3760235')
('a', '(NLNZils)6278')
('a', '(NLNZils)6278-ilsdb')
('a', '(OCoLC)957343')
('d', 'WN*')
('a', 'nznb')
('a', 'PN5596.B3')
...
```
For brevity we've only shown the first few fields. 

# Magic PyMARC methods... 

Pymarc helps us out by providing a few useful methods that allow us to get fields and subfields much more elegantly. 

Firstly, <code>get_fields()</code>:


```Python
for record in reader:
	my_500s = record.get_fields('500')
	for my_500 in my_500s:
		print (my_500)
```

Before you consider the output of this code, consider the structure of the code itself. 

Can you see any coding conventions being used?  What are they? Why are they being used? 
___
```
=500  \\$aEric Baume was a New Zealander.
=500  \\$aIncludes index.
=500  \\$aAvailable from Fiesta Products, Christchurch, N.Z.
=500  \\$aIncludes index.
=500  \\$aCover title.
=500  \\$a"December 1992."
=500  \\$aCover title.
=500  \\$aSpine title: Chilton Saint James : 75 years.
=500  \\$aAvailable from Chilton Saint James School, P.O. Box 30090, Lower Hutt, N.Z.
=500  \\$aSpine title: 50 years of Tatum Park.
=500  \\$aCaption title.
=500  \\$a"March 1993"--Cover.
=500  \\$aCover title: Discussion document by the Working Party on Fire Service Levy.
=500  \\$a"Chaired by ... David Harrison."
=500  \\$aChiefly statistical tables.
=500  \\$a"New Zealanders' living arrangements, including their household composition and family type characteristics are the focus of this report. Information on private dwellings is also included"--Back cover.
=500  \\$aCover title: 1991 census of population and dwellings : New Zealanders at home.
=500  \\$aSpine title: Census 1991 : New Zealanders at home.
=500  \\$aOn cover: Census '91.
=500  \\$aInvalid ISSN on t.p. verso.
=500  \\$aIncludes advertising.
=500  \\$a"Catalogue number 02.226.0091"--T.p. verso.
```

We're not limited to one field in this method:

```Python
for record in reader:
	my_500s = record.get_fields('500', '700')
	for my_500 in my_500s:
		print (my_500)
```
____
```
=500  \\$aEric Baume was a New Zealander.
=500  \\$aIncludes index.
=500  \\$aAvailable from Fiesta Products, Christchurch, N.Z.
=700  10$aGoodliffe, J. D.$d(John Derek)
=500  \\$aIncludes index.
=500  \\$aCover title.
...
```


Lets unpick a field that contains subfields:

```Python
for record in reader:
    my_245s = record.get_fields('245')
    for my_245 in my_245s:
        my_245_subfields = my_245.get_subfields('a', 'b', 'c', 'f', 'g', 'h', 'k', 'n', 'p', 's', '6', '8')
        for my_245_subfield in my_245_subfields:
            print (my_245_subfield)
    quit()

```
____
```
Larger than life :
the story of Eric Baume /
by Arthur Manning. 
```
We need to specify the field codes, or subfield codes for both of these methods. The list of subfield codes was made by refering to the MARC data page for the 245 field https://www.loc.gov/marc/bibliographic/concise/bd245.html

There one more trick to pymarc that helps us to parse a MARC record. In a previous episode we looked at the sturcture of MARC files, and noted where we can see the two indicators for any field. We can get to this data directly via pymarc: 

```Python
for record in reader:
	print (record['245'])
	print ("Field 245 indicator 1: {}".format(record['245'].indicator1))
	print ("Field 245 indicator 2: {}".format(record['245'].indicator2))
	quit()
```
_____
```
=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
Field 245 indicator 1: 1
Field 245 indicator 2: 0
```

We can use use this as another searching tool:

```Python
for record in reader:
	ind_2 =  record['245'].indicator2
	if ind_2 != '0':
		print (record['245'])
		print ()
```
_____
```
=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
Field 245 indicator 1: 1
Field 245 indicator 2: 0
```

# List of PyMARC methods associated with a record object

The pymarc record object has more useful data "shortcuts" that we won't go into the specifics of, but are useful to know. These are all prebuilt methods that get you to key data in a record, assuming (a) its been entered in the record and (b) its been entered in a way the library developers expected.  

```Python
record.author()
record.isbn()
record.issn()
record.issn_title()
record.leader
record.location()
record.pos
record.publisher()
record.pubyear()
record.series()
record.sudoc()
record.title()
record.uniformtitle()
record.notes()
record.subjects()
record.physicaldescription()
```

If you have time, see what happens when you use these "shortcuts" to access bits of data in the pymarc record object. Try looking at record and matching the data item you see, with the original record:

```Python
for record in reader:
	print (record)
	print ("\n______________________________\n\n")
	print (record.author())
	print (record.isbn())
	print (record.issn())

	quit()

# Building a basic parser!

We could pull some of the approaches we looked at into a single script:

```Python
    for record in reader:
        print ("MMS ID:", record['001'].value())
        for my_field in record:
            #### Control fields (in the range 00x) don't have indicators. 
            #### We use this try/except catcher to allow us to elegantly handle both cases without encountering a breaking error, or a coding failure
            try:  
                ind_1 = my_field.indicator1
                ind_2 = my_field.indicator2

                #### Setting an empty indicator to a more conventional and readable "/"
                if ind_1 == " ":
                    ind_1 = "/"
                if ind_2 == " ":
                    ind_2 = "/"

                print ("\tTag #:", my_field.tag, "Indicator 1:", ind_1 , "Indicator 2:", ind_2)
            except AttributeError:
                print ("\tTag #:", my_field.tag)

            for my_subfield_key, my_subfield_value in my_field:
                print ("\t\t", my_subfield_key, my_subfield_value)
            print ()
        print ()
        quit()
```
____
```
MMS ID: 9962783502836
	Tag #: 001

	Tag #: 003

	Tag #: 005

	Tag #: 008

	Tag #: 035 Indicator 1: / Indicator 2: /
		 z 4260

	Tag #: 035 Indicator 1: / Indicator 2: /
		 a (nzNZBN)687856

	Tag #: 035 Indicator 1: / Indicator 2: /
		 9    67095940

	Tag #: 035 Indicator 1: / Indicator 2: /
		 a (Nz)3760235

	Tag #: 035 Indicator 1: / Indicator 2: /
		 a (NLNZils)6278

	Tag #: 035 Indicator 1: / Indicator 2: /
		 a (NLNZils)6278-ilsdb

	Tag #: 035 Indicator 1: / Indicator 2: /
		 a (OCoLC)957343

	Tag #: 040 Indicator 1: / Indicator 2: /
		 d WN*

	Tag #: 042 Indicator 1: / Indicator 2: /
		 a nznb

	Tag #: 050 Indicator 1: 0 Indicator 2: /
		 a PN5596.B3
		 b M3
	...
```
Have a play around with a building a parser that displays data that you're interested in, using the above as a template. 

**Experiments!**

See if you can find any records with the OCLC identifier "39818086"
Can you count how many records have more than one 500 fields?
#todo - what is the main language indicator!?
Can you find out how many records describe an item thats written in English? (hint: We can look in the <code>record.leader</code> in position )
