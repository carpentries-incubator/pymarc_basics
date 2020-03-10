---
title: Parsing with PyMARC - PArt Two
teaching: 30
exercises: 30
objectives:
- Finding specific fields with pymarc
- finding specific data with pymarc
keypoints:
- We can search for specific information in a set of MARC records. 
- We understand how to explore fields, indicators and subfields in any MARC record.  
---
## Episode 3: Parsing with pymarc

# Finding specific fields with PyMARC

Carry on with the script file from the previosu episode <code>episode_3.py</code>

Lets keep looking at searching. 

What about if we want any record that contains the string "New Zealand"? How might we adapt the code? 

```python
	if "New Zealand" in str(record):
		print (record) 
		print()
```

This could result in an overwhelming amount of data if we're not careful. Lets have a think about how we might frame that question in a way that helps to refine the data into a useful form. 

What happens if we  ask to see any MARC field that contains our search string. We can do this by adding another loop. 
We also might want to think about how we associate each match with a particular record. One way of doing this would be to print the record ID as well as the matching field:

```python
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
{: .output}


We can use the same loop/iterator approach to process any field that has subfields. Lets see what that looks like:

```python
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
{: .output}

For brevity we've only shown the first few fields. 

# Magic PyMARC methods... 

Pymarc helps us out by providing a few useful methods that allow us to get fields and subfields much more elegantly. 

Firstly, <code>get_fields()</code>:


```python
for record in reader:
	my_500s = record.get_fields('500')
	for my_500 in my_500s:
		print (my_500)
```

Before you consider the output of this code, consider the structure of the code itself. 

> ## Coding conventions 
> Can you see any coding conventions being used?  What are they? Why are they being used? 
> > ## Solution
> > In coding there are some strong rules about things we can/can't do. These are important because if we don't follow these rules our code doesn't work. This includes things like not starting variable names with numbers or trying to use reserved terms like <code>=</code> in ways that the complier can't process. 
> >
> > There are also coding conventions. These are less strict rules, but equally important. These are usually followed to aid readability, portability and shareability of our code. Pep 8 is a useful start for learning about common conventions [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
> > 
> > Conventions can also be quite personal, or agreed by a coding group. 
> >
> > In this script when we're making 'iterables' (things that contain other things, like lists or dictionaries) we always pluralise the variable name e.g. <code>for thing in <b>things</b></code>. This helps us to know the data type we are using. 
> >  
> > In this script we're adding the text "my_" to any item we're creating. Its a convention thats used to show that the item being made/used "belongs" to a particular method. Its not something we need to pay particular attention to, but it is useful to notice it in code as we start to explore Python scripts.  
> > 
> {: .solution}
{: .challenge}

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
{: .output}


We're not limited to one field in this method:

```python
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
{: .output}



Lets unpick a field that contains subfields:

```python
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
{: .output}

We need to specify the field codes, or subfield codes for both of these methods. The list of subfield codes was made by referring to the MARC data page for the 245 field [https://www.loc.gov/marc/bibliographic/concise/bd245.html](https://www.loc.gov/marc/bibliographic/concise/bd245.html)

There one more trick to pymarc that helps us to parse a MARC record. In a previous episode we looked at the structure of MARC files, and noted where we can see the two indicators for any field. We can get to this data directly via pymarc: 

```python
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
{: .output}

We can use use this as another searching tool:

```python
for record in reader:
	ind_2 =  record['245'].indicator2
	if ind_2 != '0':
		print (record['245'])
		print ()
```
_____
```
=245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.

=245  04$aThe Discussion document of the Working Party on Fire Service Levy /$b... prepared by the Working Party on the Fire Service Levy.
```
{: .output}


# List of PyMARC methods associated with a record object

The pymarc record object has more useful data "shortcuts" that we won't go into the specifics of, but are useful to know. These are all pre-built methods that get you to key data in a record, assuming (a) its been entered in the record and (b) its been entered in a way the pymarc developers expected to find it.  

```python
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

If you have time, see what happens when you use these "shortcuts" to access bits of data in the pymarc record object. 

Try looking at record and matching the data item you see, with the original record:

```python
for record in reader:
	print (record)
	print ("\n______________________________\n\n")
	print (record.author())
	print (record.isbn())
	print (record.issn())

	quit()
```

# Building a basic parser!

We can arrange some of the approaches we've looked at into a single script:

```python
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
{: .output}

Have a play around with a building a parser that displays data that you're interested in, using the above as a template. 


> ## Experiments!
> What is the 001 identifier for the record with the OCLC identifier 39818086?
>
> How many records have more than one 500 fields?
>
> how many records describe an item with English as the primary language? (hint: We can look in the <code>record['008']</code> field to find out the primary language)
> > ## Solution
> > (a) 99628093502836
> > 
> >~~~
> >for record in reader:
> >	for f in record.get_fields('035'):
> >		if "39818086" in f.value():
> >			print (record['001'].value())
> >~~~ 
> > 
> > (b) 4
> >
> >~~~ 
> >for record in reader:
> >	my_500s = record.get_fields('500')
> >	print (len(my_500s))
> >~~~
> > 
> > (c) 10
> >
> >~~~
> >for record in reader:
> >	if "eng" in record['008'].value():
> >		print (record['008'])
> >~~~
> {: .solution}
{: .challenge}



{% include links.md %}