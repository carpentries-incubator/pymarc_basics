---
title: Parsing with PyMARC - Part One
teaching: 30
exercises: 30
objectives:
- How to read a marc record with pymarc
- Finding specific fields with pymarc
keypoints:
- We can print out any field from a MARC record we are interested in. 
- We can search for specific information in a set of MARC records. 
---
## Episode 3: Parsing with pymarc

# Finding specific fields with PyMARC

Start a new file in your IDE <code>episode_3.py</code>

Set up the basic record reader like we did in episode 2:


```python
from pymarc import MARCReader

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        print (record)
```


We can used the data object created by pymarc to only process fields we're interested in. We can do that by telling python the field name/label we're interested in e.g. <code>print (record['245'])</code> In this piece of code we're asking pymarc to print any field in our record object that has the label/name <code>245</code>  

If we add this piece of code to our basic file parser we can see all the title statements for our test set:

```python
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
{: .output}



> ## Understanding Python data types and data objects
>
> What data type does the record object appear to be?
>
> Hint: <code>print (type(record))</code>
> > ## Solution
> >
> > The record object that PyMARC creates looks like its an instance of the python data type called a dictionary. 
> >
> > Getting used to what data types look like, and how to 'ask Python' what they actually are important skills to develop. 
> >
> > We can ask python to tell us what the data type is of any object using the <code>type()</code> function. Doing this reveals that the record is a <code>class</code> object - <code><class 'pymarc.record.Record'></code>. 
> >
> > Once we've spent a little time around python code, we might guess that the record item is a particular data type called a dictionary or <code>dict()</code>. The main clue we might rely on is the square brackets after the object name. e.g <code>my_dict['my_dict_key']</code>
> > 
> > We're not going to spend serious time in this lesson exploring either <code>class</code> or <code>dict</code> structures in this lesson. 
> >If you're interested to learn more about them there are many free resources that can help, like [https://www.tutorialspoint.com/python/python_data_structure.htm](https://www.tutorialspoint.com/python/python_data_structure.htm)
> {: .solution}
{: .challenge}


Behind the scenes when this script is run, python looks at the data object that pymarc created, and looks for the part of it that has the label, or 'key' of "245". 

See what happens if you give it a key that isn't included in the data object:


```python
for record in reader:
	print (record['this_key_doesnt_exist'])
	quit()
```
___
```
None

```
{: .output}


Notice it doesn't give you an error or otherwise strongly signal that it did not find the key you're interested in the data object. Its useful to know this happens if we use an key that doesn't exist. If you see the return <code>None</code> in your scripts where you are expecting an actual value, double check the key you've used. Common errors would be typos (e.g. <code>record['254']</code> instead of <code>record['245']</code>) or using a number instead of a string (e.g. <code>record[245]</code> instead of <code>record['245']</code>).

In this case, returns <code>None</code>, which itself is an important concept in Python. Its worth pausing for a moment and making sure we understand what <code>None</code> means in the Python context. 

>The None keyword is used to define a null value, or no value at all.
>
>None is not the same as 0, False, or an empty string. 
>
>None is a datatype of its own (NoneType) and only None can be None."

[https://www.w3schools.com/python/ref_keyword_none.asp](https://www.w3schools.com/python/ref_keyword_none.asp) 

# Accessing Subfields

We can use the same 'key' method to get to any subfields we might have:

```python
for record in reader:
	print ("Subfield 'a':", record['245']['a'])
	print ("Subfield 'b':", record['245']['b'])
	print ("Subfield 'c':", record['245']['c'])
	quit()
```

Notice how we're asking for 3 things in each of these print statements. We're asking python to look in the data object called <code>record</code>. We're asking for the part of that item that has the key <code>'245'</code>. Within that subset of the <code>record</code> object, we're further asking for the part that has the key <code>'a'</code>, <code>'b'</code> or <code>'c'</code> 
_____

```
Subfield 'a': Larger than life :
Subfield 'b': the story of Eric Baume /
Subfield 'c': by Arthur Manning.
```
{: .output}


> ## Nuance of punctuation use in MARC
>
> What do you notice about these pieces of data? 
> > ## Solution
> > The text we see is three individual bits of text. They are not particularly well connected to each other in this form - we need to process all of the 245 field as a whole to make sure we're operating on the data we're expecting. 
> >
> > Notice the punctuation that is included in the text. We might need to do something to clean that up if we're going to further process the data we find in this field. The use of punctuation marks within a piece of information to indicate specific parts within the data item is not limited to the 245 field. We can see it variously throughout the MARC record. 
> > "In the past, catalogers recorded bibliographic data as blocks of text and used punctuation to demarcate and provide context for the various data elements. This made data understandable to users when it was presented on cards and in online catalogs."
> > [https://www.loc.gov/aba/pcc/documents/PCC-Guidelines-Minimally-Punctuated-MARC-Data.docx](https://www.loc.gov/aba/pcc/documents/PCC-Guidelines-Minimally-Punctuated-MARC-Data.docx)
> > This is one of the interesting challenges we face when processing MARC records in bulk/computationally. These punctuation marks have a strong historical place in cataloging practice, and as a result, they're an artifact we need to be aware of and deal with computationally.
> {: .solution}
{: .challenge}


> ## Considerations when working with related subfields
> What might we need to consider if we want to use data that potentially spans multiple subfields? 
> > ## Solution
> >Supposing we want to try and match title of an item with a MARC record, and a list of book titles we've been given to compare we might find ourselves with a problem.   
> >
> >How do we know which of the subfields is the right amount data to search for a match? This isn't a new problem for libraries - its another facet of any deduping process! For us working in the MARC record via python, we have to be aware of the data we're using, both inside the MARC, and that we're trying to match against. We might need to join two or more fields. We might need to remove the catalogers punctuation to help with clean matching.   
> {: .solution}
{: .challenge}

There are a few other ways we can get to the same data that are worth exploring. 

The data object that pymarc creates has a method called "<code>value()</code>". We can use this to return the data field as text string without any subfield markers or indicators. 

This is also a good opportunity to explore that "<code>type()</code>" method. 

PyMARC gives us some convenient keywords to help us access key bits of data. One of those is the keyword <code>.title()</code>. 

Lets have a look a one record and what these various methods produce:

```python
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
{: .output}


We can use a similar approach to find a particular record. Lets say we're looking for the record with the 001 identifier of <code>99628153502836</code>. We can loop through the records in our <code>pymarc.reader</code> object and look for a match:

```python
	for record in reader:
		if record['001'].value() == str(99628153502836):
			print ("Success! found record with id 99628153502836")
```

We can make this a little more useful by abstracting the search id into a variable:

```python
	search_id = 99628153502836
	for record in reader:
		if record['001'].value() == str(search_id):
			print ("Success! found record with id {}.format(search_id)")
```

> ## Using variables in code
> What is main difference between these two code snippets? Why is it useful?
> > ## Solution
> > In the first example we're hard coded the text we want to search for. Both in the search itself, and the successful response. 
> > In the second example we've used a variable to hold the identifier. This gets reused in both the search, and the successful response.   
> >
> >By doing this we've made the code much more useful. We can reuse the same code and answer more questions just by changing one variable. This is a good basic process to use when you're writing your code. Untangling hard coded values can be a very time consuming and confusing process  
> {: .solution}
{: .challenge}


> ## More on data types... 
> Why do we need the <code>str()</code> conversion? Can you think of a different way of solving the same problem?
> > ## Solution
> >In Python the string <code>"1234"</code> is not the same as the integer <code>1234</code>.  When trying to match data with python we have to be careful to make sure we are matching across data types e.g. strings with strings, or integers with integers. If we don't we will miss matches. 
> >
> > We didn't have to convert the search term <code>search_id</code> into a string. We equally could have turned the record ID data into a integer <code>if int(record['001'].value()) == search_id</code>
> >
> > There are pros and cons for each approach. The main thing we should be aware of is that numbers and strings are different things, and <i>numbers as strings</i> is a particularly common problem to encounter. 
> {: .solution}
{: .challenge}

Lets make our search a little more interesting. Lets say we're interested in in any record that contains the string "New Zealand" in the <code>245</code> field

```python
    if "New Zealand" in record['245'].value():
        print (record['245'])
```
_____
```
	=245  00$aThese fortunate isles :$bsome Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /$cselected, translated and annotated by John Goodliffe.
	=245  02$aA Statistical profile of young women /$ccompiled for the YWCA of Aotearoa-New Zealand by Nic Mason, Dianna Morris and Angie Cairncross ; with the assistance of Shell New Zealand.
	=245  00$a1991 New Zealand census of population and dwellings.$pNew Zealanders at home.
```
{: .output}


Lets have a look at what happens if we use the <code>.title()</code> method as our string that we're searching:

```python
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
```
{: .output}

Notice this difference between these two scripts. This is a really good example of a paradigm we find in coding, explicit vs implicit. 

>In programming, implicit is often used to refer to something that’s done for you by other code behind the scenes. 
>Explicit is the manual approach to accomplishing the change you wish to have by writing out the instructions to be done explicitly.

[https://blog.codeship.com/what-is-the-difference-between-implicit-vs-explicit-programming/](https://blog.codeship.com/what-is-the-difference-between-implicit-vs-explicit-programming/)

In this case, the programmers behind the pymarc library have made some choices about which version of a title they think is the most straightforward. This is based on what the MARC standard says about a title, and how to interpret the field as a human being. 
We don't necessarily know what those choices where, we simply trust that they made sensible one! This is an example of implicit coding. If we built our title parser, that read the field, and its associated subfields, and used some logic to turn that data into a single string like <code>record.title()</code> does, we would be explicitly coding this solution. 