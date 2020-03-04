---
title: Changing a record with PyMARC
teaching: 30
exercises: 30
objectives:
- How to delete some information from a record
- How to add some information from a record
- How to change some information in a record
- How to make a new record 
keypoints:
- We can manipulate a MARC record with PyMARC
- We can add a field to record
- We can change the information in a record
- We can make a new record 
---
Episode 4: Parsing with pymarc

Start a new file in your IDE <code>episode_4.py</code>

Set up the basic record reader like we have previously, this time we're only going to process one record: 

```Python
from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)

```

Let set up a parser that will allows us to manipulate a single record. We already know we're going to reuse this parser for the rest of this episode, so lets make sure we start with something thats well built. 

As we know we will be changing a record in some way we'll probably want to copy the record to a new object, and make our changes on that. Python has a particular trait around copying objects that we need to be aware of. If we use the basis assignation via an equals sign - <code>a = b</code> behind the scenes python essentially make a new pointer to original object. This means that <code>a</code> is not a copy of <code>b</code>, it IS <code>b</code>! Any changes to <code>b</code> are also in <code>a</code>. We can check this by asking python to tell us the internal identifier it uses to track the various objects: 

```Python
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

Your id number will be different to the one shown here, they are assigned by python at run time.   

To make sure we make a new record that we can change without making changes to the original record we can use the python <code>deepcopy()</code> method to solve the problem: 

```Python
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

Lets look at how we can change an existing piece of information in a record. Currently in our record we can see we have an author noted as Arthur Manning. As an exercise, lets say that Arthur informed us that he isn't infact the author, his twin sister, Arthuretta is. We need to change this record to make sure its accurate! 

```python
    for record in reader:
        my_record = deepcopy(record)

        # we only need to update the 'a' subfield.
        # note the catalogers punctuation... we must include the commas. 
        my_record['100']['a'] = "Manning, Arthuretta,"

        #comparing the two
        print (my_record['100'])
        print (record['100'])

        quit()
```

> ## Try for yourself
>
> How would you change the date of birth date in the 'd' subfield to 1920?
> > ## Solution
> ><code>my_record['100']['d'] = "1920-"</dode>
> {: .solution}
{: .challenge}


{% include links.md %}