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
Episode 4: Parsing with pymarc

Start a new file in your IDE <code>episode_4.py</code>

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

```python
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


Lets look at how we might choose the field we want to delete when there are more than one. Lets delete the 035 field that contains the text "ilsdb" <code>=035  \\$a(NLNZils)6278-ilsdb</code>:

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
~~~
7
6
~~~
{. output}

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
{. output}








{% include links.md %}