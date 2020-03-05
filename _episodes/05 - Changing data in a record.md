---
title: Changing a record with PyMARC
teaching: 30
exercises: 30
objectives:
- How to change some information in a record
- How to delete some information from a record
- How to add some information from a record
- How to make a new record 
keypoints:
- We can manipulate a MARC record with PyMARC
- We can change the information in a record
- We can add a field to record
- We can make a new record 
---
Episode 5: Parsing with pymarc

Start a new file in your IDE <code>episode_5.py</code>

Set up the basic record reader like we have previously, this time we're only going to process one record: 

```python
from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)

```

Let set up a parser that will allows us to manipulate a single record. We already know we're going to reuse this parser for the rest of this episode, so lets make sure we start with something thats well built. 

As we know we will be changing a record in some way we'll probably want to copy the record to a new object, and make our changes on that. Python has a particular trait around copying objects that we need to be aware of. If we use the basis assignation via an equals sign - <code>a = b</code> behind the scenes python essentially make a new pointer to original object. This means that <code>a</code> is not a copy of <code>b</code>, it IS <code>b</code>! Any changes to <code>b</code> are also in <code>a</code>. We can check this by asking python to tell us the internal identifier it uses to track the various objects: 

```python
a = ["Hello"]
# assigning b to be a
b = a
#printing b
print ("b =", b)
print (id(a))
print (id(b))
print ()

#changing a *only*!
a[0] = "World!"
#printing b
print ("b =", b)
print (id(a))
print (id(b))
```
____
```
b = ['Hello']
1983706174528
1983706174528

b = ['World!']
1983706174528
1983706174528
```
{: .output}

Your id number will be different to the one shown here, they are assigned by python at run time.   

To make sure we make a new record that we can change without making changes to the original record we can use the python <code>deepcopy()</code> method to solve the problem: 

```python
from pymarc import MARCReader
from copy import deepcopy

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
	reader = MARCReader(data)
	for record in reader:
		my_record = deepcopy(record)

		print (id(record))
		print (id(my_record))

		quit()

```

Lets look at how we can change an existing piece of information in a record. Currently in our record we can see we have an author noted as Arthur Manning. 

As an exercise, lets say that Arthur informed us that he isn't in fact the author, his twin sister] - Arthuretta is. We need to change this record to make sure its accurate! 


```python
    for record in reader:
        my_record = deepcopy(record)

        # we only need to update the 'a' subfield.
        # note the catalogers punctuation... we must include the commas. 
        my_record['100']['a'] = "Manning, Arthuretta,"

        #comparing the two
        print (record['100'])
        print (my_record['100'])

        quit()
```
___
```
=100  1\$aManning, Arthur,$d1918-
=100  1\$aManning, Arthuretta,$d1918-
```
{: .output}

Note: of course, the MARC 100 field is an authorised person - so we shouldn't really do this unless there is an authority file for this new person! 

> ## Try for yourself
>
> How would you change the date of birth date in the 'd' subfield to 1920?
> > ## Solution
> ><code>my_record['100']['d'] = "1920-"</code>
> {: .solution}
{: .challenge}

# Removing information from a record

Lets see how we can remove a field. As an exercise lets say we need to remove the 300 field: 

```python
for record in reader:
    my_record = deepcopy(record)

    # We use the get_fields() method to generate a list of 300 get_fields
    # As there is only, we can just remove it. 
    for my_field in my_record.get_fields('300'):
        my_record.remove_field(my_field)

    #comparing the two
    print (record['300'])
    print (my_record['300'])

    quit()
```

This seems pretty straightforward. This is a simple case - there is only one 300 field, so we don't need to do anything else to make sure we're doing what we intended. One of the things to be aware of when we're processing in bulk is writing scripts that have unintended consequences... 

> ## Unintended consequences
>
> What do you think would happen if we used a field that has more than one, like 035?
> > ## Solution
> >They would all be removed.
> {: .solution}
{: .challenge}

One of the ways we try and mitigate unintended consequences is to build in checks to our script that help ensure that we only process things that fit our criteria. In this case the criteria is very simple, we want to delete the 300. There is actually a 'hidden' criteria that we're implicitly addressing.  


> ## Unintended consequences - implicit requirements
>
> What is the implicit requirement 'hidden' in the task "remove the 300 from our record"? What would be the impact of this on our process?
> > ## Solution
> > There might be an assumption that there is only one 300 field. If we assumed there was only ever one 300 field, and didn't check, we might remove more fields than we expected to.  
> {: .solution}
{: .challenge}

We have a few strategies to help with this problem.

1. Check the standard. It may be that there is only one 300 field allowed in the record. This doesn't always help - we may find non standards compliant records!
2. Check the corpus. It might be sensible to check the dataset we are working with to test what we find in our records. 
3. Use some logic checks in our scripts to ensure we only remove 300 from a record where there is only one found in record. 

Lets look at what #3 looks like in script. 

```Python
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)

        # We use the get_fields() method to generate a list of 300 get_fields
        my_fields = my_record.get_fields('300')
        
        # We test if this list of fields contains only one member
        if len(my_fields) == 1:
            print ("Only one 300 field found in record ID {}. Removing it.".format(record['001'].value()))
            for my_field in my_fields:
                my_record.remove_field(my_field)
        else:
            print ("More than one 300 field found in record ID {}. Doing nothing.".format(record['001'].value()))

        # comparing the two
        print ("Number of 300 fields in record:", len(record.get_fields('300')))
        print ("Number of 300 fields in my_record:", len(my_record.get_fields('300')))
        print()

        # testing the failing case 

                # We use the get_fields() method to generate a list of 300 get_fields
        my_fields = my_record.get_fields('035')
        
        # We test if this list of fields contains only one member
        if len(my_fields) == 1:
            print ("Only one 035 field found in record ID {}. Removing it.".format(record['001'].value()))
            for my_field in my_fields:
                my_record.remove_field(my_field)
        else:
            print ("More than one 035 field found in record ID {}. Doing nothing.".format(record['001'].value()))

        # comparing the two
        print ("Number of 035 fields in record:", len(record.get_fields('035')))
        print ("Number of 035 fields in my_record:", len(my_record.get_fields('035')))

        quit()
```
___
~~~
Only one 300 field found in record ID 9962783502836. Removing it.
Number of 300 fields in record: 1
Number of 300 fields in my_record: 0

More than one 035 field found in record ID 9962783502836. Doing nothing.
Number of 035 fields in record: 7
Number of 035 fields in my_record: 7

~~~
{: .output}


Lets look at how we might choose the field we want to delete when there are more than one. Lets delete the 035 field that contains the text "ilsdb". 

We can do that by testing for the presence of the string "ilsdb" in our various 035 fields. 

We're starting with these 035 fields - we can see that only one field has "ilsdb" in it, so its a safe test to use in this case: 

~~~
=035  \\$z4260
=035  \\$a(nzNZBN)687856
=035  \\$9   67095940
=035  \\$a(Nz)3760235
=035  \\$a(NLNZils)6278
=035  \\$a(NLNZils)6278-ilsdb
=035  \\$a(OCoLC)957343
~~~
{: .output} 

```Python
for record in reader:
    my_record = deepcopy(record)

    print (record)

    my_fields = my_record.get_fields('035')
    for my_field in my_fields:
        if "ilsdb" in my_field.value():
            my_record.remove_field(my_field)


    print (len(record.get_fields('035')))
    print (len(my_record.get_fields('035')))

    quit()
```
____

~~~
7
6
~~~
{: .output}

We end up with these:

~~~
=035  \\$z4260
=035  \\$a(nzNZBN)687856
=035  \\$9   67095940
=035  \\$a(Nz)3760235
=035  \\$a(NLNZils)6278
=035  \\$a(OCoLC)957343
~~~
{: .output}  

This is only one approach of many to tackling this task. For any given task the solution might require checking field indicators, other fields, text in subfields etc. 

We can use a very similar approach to removing subfields. Lets remove the 'b' subfield from the 100 field: 

```Python
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        my_fields = my_record.get_fields('100')
        for my_field in my_fields:
            my_field.delete_subfield('d') 

        print (record['100'])
        print (my_record['100'])

        quit()
```
~~~
=100  1\$aManning, Arthur,$d1918-
=100  1\$aManning, Arthur,
~~~
{: .output}

# Adding information to a record

Lets look at how we can add a new field to a record. To do this we, we need to make a pymarc field object, and add it to the record. There are two different types of field in pymarc, a control field, and a non control field.   

We can use the pymarc documentation to see how we can make a field data object:

```Python
from pymarc import Field

print (help(Field))
```

~~~
Help on class Field in module pymarc.field:

class Field(builtins.object)
 |  Field(tag, indicators=None, subfields=None, data='')
 |  
 |  Field() pass in the field tag, indicators and subfields for the tag.
 |  
 |      field = Field(
 |          tag = '245',
 |          indicators = ['0','1'],
 |          subfields = [
 |              'a', 'The pragmatic programmer : ',
 |              'b', 'from journeyman to master /',
 |              'c', 'Andrew Hunt, David Thomas.',
 |          ])
 |  
 |  If you want to create a control field, don't pass in the indicators
 |  and use a data parameter rather than a subfields parameter:
 |  
 |      field = Field(tag='001', data='fol05731351')
 ...
 ~~~
 {: .output} 

Ok, so it looks like we need to pass the <code>Field()</code> method the tag we want to use, the indicators, and the subfield data. Lets have go!


```Python 
from pymarc import Field 

with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
        ### making the new 245 field
        my_new_245_field = Field(

                            tag = '245', 

                            indicators = ['0','1'],

                            subfields = [
                                            'a', 'The pragmatic programmer : ',
                                            'b', 'from journeyman to master /',
                                            'c', 'Andrew Hunt, David Thomas.',
                                        ]
                            ) 
        ### adding the new field
        my_record.add_ordered_field(my_new_245_field)

        ### showing the diffence
        for original_245 in record.get_fields('245'):
            print (original_245)
     
        print ("______")

        for my_record_245 in my_record.get_fields('245'):
            print (my_record_245)

        quit()
```

~~~

=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
______
=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
=245  01$aThe pragmatic programmer : $bfrom journeyman to master /$cAndrew Hunt, David Thomas.
~~~
{: .output}

Lets have a look at the whole new record and double check things.

```Python
print (my_record)
```

~~~
=245  10$aLarger than life :$bthe story of Eric Baume /$cby Arthur Manning.
=245  01$aThe pragmatic programmer : $bfrom journeyman to master /$cAndrew Hunt, David Thomas.
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
=245  01$aThe pragmatic programmer : $bfrom journeyman to master /$cAndrew Hunt, David Thomas.
~~~
{: .output}

Notice where the new field is. The <code>add_field()</code> method has added it to the end of the record.  

> ## Order of fields in a MARC record
>
> Does a MARC record need to be sorted into 'proper' numerical order?
> > ## Solution
> >Sometimes it will, sometimes it won't. As a data object the order doesn't necessary need to be sorted numerically The MARC standard only stipulates that control fields have to come before data fields  - ["Structure of a MARC 21 Record"](https://www.loc.gov/marc/specifications/specrecstruc.html). As human readers we expect the item to be numerical. And its not unreasonable to assume that some downstream tool might expect the fields to be numerically sorted. 
> {: .solution}
{: .challenge}

If we want to ensure our new field is added in the correct numerical sort position we use the <code>add_ordered_field()</code> method:

```Python
for record in reader:
    my_record = deepcopy(record)
    ### making the new 245 field
    my_new_245_field = Field(

                        tag = '245', 

                        indicators = ['0','1'],

                        subfields = [
                                        'a', 'The pragmatic programmer : ',
                                        'b', 'from journeyman to master /',
                                        'c', 'Andrew Hunt, David Thomas.',
                                    ]
                        ) 
    ### adding the new field
    my_record.add_ordered_field(my_new_245_field)
```

While we're thinking about validation / what we expect our records to look like, its worth knowing that PyMARC doesn't do much (anything...) by the way of data validation. t won't prevent you from making a MARC item that isn't compliant with the MARC standards. 

# Making a new record

Lets do one last task, and make a new record. 

```Python
from pymarc import Record

my_new_record = Record()

print (my_new_record)
```

~~~
=LDR            22        4500
~~~
{: .output}

Its that straight forward! We've made a new empty record. All it contains is a minimum LEADER data required by a MARC record.

 > ## Try for yourself
>
> Make a record that contains the following information
>
> 001: a, 
>
>
>
>
>
>
> > ## Solution
> ><code>my_record['100']['d'] = "1920-"</code>
> {: .solution}
{: .challenge}

{% include links.md %}