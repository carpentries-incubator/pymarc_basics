---
title: "MARC basics"
teaching: 0
exercises: 0
objectives:
- What is MARC?
- Where are helpful resourse for MARC?
- Understanding the basic structure of a MARC file in pymarc
---
Episode 2: MARC basics

"MARC is the acronym for **MA**chine-**R**eadable **C**ataloging. It defines a data format that emerged from a Library of Congress-led initiative that began nearly forty years ago. It provides the mechanism by which computers exchange, use, and interpret bibliographic information, and its data elements make up the foundation of most library catalogs used today. MARC became USMARC in the 1980s and MARC 21 in the late 1990s."
https://www.loc.gov/marc/

"MARC Terms and Their Definitions"
https://www.loc.gov/marc/umb/um01to06.html#part3

"This online publication provides access to both the full and concise versions of the MARC 21 Format for Bibliographic Data." http://www.loc.gov/marc/bibliographic/

Lets take a look at a marc record, and see what it contains. 

Start a new python file  <code>episode_2.py</code> and type the following script:

```Python
	import pymarc

	my_marc_file = "NLNZ_example_marc.mrc"

	reader = pymarc.MARCReader(file(my_marc_file)) 

	for record in reader:
		print (record)
		quit()
```

You should see a marc file:
```
	=LDR  00912cam a2200301 a 4500
	=001  9962783502836
	=003  Nz
	=005  20161223124839.0
	=008  731001s1967\\\\at\ac\\\\\\\\\00010beng\d
	=035  \\$z4260
	=035  \\$a(nzNZBN)687856
	=035  \\$9   67095940
	=035  \\$a(Nz)3760235
	=035  \\$a(NLNZils)6278
	=035  \\$a(NLNZils)6278-ilsdb
	=035  \\$a(OCoLC)957343
	=040  \\$dWN*
	=042  \\$anznb
	=050  0\$aPN5596.B3$bM3
	=082  0\$a823.2$220
	=100  1\$aManning, Arthur,$d1918-
	=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
	=260  \\$aSydney [N.S.W.], :$aWellington [N.Z.] :$bReed,$c1967.
	=300  \\$a184 p., [8] p. of plates :$bill., ports. ;$c23 cm.
	=500  \\$aEric Baume was a New Zealander.
	=600  10$aBaume, Eric,$d1900-1967.
	=650  \0$aJournalists$zAustralia$xBiography.
	=650  \0$aAuthors, New Zealand$y20th century$xBiography. 
```

Its useful to understand the structure of the data object we can see, and how it relates to the MARC format. 

Notice the first piece of data starts with an <kbd>=</kbd>. The first one we see is <code>=LDR</code>. The <code>=</code> tells us its a field label, or tag, and the following 3 characters are the tag value. In this case <code>LDR</code> tells us we're reading the leader field. All other MARC fields are zeropadded 3 digit numbers. The following data on that row is the field value. In MARC, the first 9 fields are called control fields, and are structured a little differently to all other fields. Its worth refering to the MARC guidelines to make sure we can correctly understand what the data is telling us...  http://www.loc.gov/marc/bibliographic/bd00x.html

We'll get into the details of some of the control fields later on. For now lets focus on one of the "standard" fields and take a look at how its made up. Lets look at the 245 field, the "title statement" http://www.loc.gov/marc/bibliographic/bd245.html

```
	=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
```

We've established the <code>=245</code> is telling us the field name. We can see a couple of spaces, and then the digits <code>1</code> and <code>0</code>. These are the two 'indicators' for the field. Sometimes they're empty or blank, some times they're unused (and encountered as the <code>\</code>) character, and sometimes they're set to a value like we can see here. We'll look at how parse this infomation later. 

Following the two indicators, we can see some data thats separated by the <code>$</code> character:

```
	$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
```

The <code>$</code> is always followed by another character, the subfield label, and then the value of the subfield. In this instance we can see 3 subfields; a, b, and c:

```
	a| Larger than life :
	b| the story of Eric Baume /
	c| by Arthur Manning.
```

Spend a moment looking at the MARC specs for this field, and the data we have in this record

http://www.loc.gov/marc/bibliographic/bd245.html