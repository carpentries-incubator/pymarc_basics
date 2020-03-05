---
title: Saving MARC Files
teaching: 5
exercises: 15
objectives:
- How to save MARC records
keypoints:
- We can save a MARC record to a suitable format
- We can save MARC records to a suitable format 
---
Episode 6: Saving MARC Files pymarc

We only have one task left. Saving our MARC records so we can ingest / use / share / etc them.  

Start a new file in your IDE <code>episode_6.py</code>

PyMARC comes with some useful tools that make this a very quick process. 

```python
from pymarc import MARCReader

my_marc_file = "NLNZ_example_marc.marc"

### We'll add records to this list. It can have a membership of 1 
my_marc_records = []
with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        ### we add out records to our list of records
        my_marc_records.append(record)
        ### and print the IDs so we can see whats happening
        print (record['001'])

# we create a new file
my_new_marc_filename = "my_new_marc_file.marc" 
with open(my_new_marc_filename , 'wb') as data:
    for my_record in my_marc_records:
        ### and write each record to it
        data.write(my_record.as_marc())

print ()
print ("___")
print ()

### we open the new marc file
with open(my_new_marc_filename, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        ### and print the IDs so we can validate we save all the records
        print (record['001'])

```

~~~
=001  9962783502836
=001  99627723502836
=001  99627923502836
=001  99628033502836
=001  99628063502836
=001  99628093502836
=001  99628113502836
=001  99628123502836
=001  99628153502836
=001  99628163502836

___

=001  9962783502836
=001  99627723502836
=001  99627923502836
=001  99628033502836
=001  99628063502836
=001  99628093502836
=001  99628113502836
=001  99628123502836
=001  99628153502836
=001  99628163502836
~~~
{: .output}

Most of the this script is helper code to show whats going!. If we strip it down to the basics, and assuming we have a list of records to save its only a few lines:

```python


my_new_marc_filename = "my_new_marc_file.marc" 
with open(my_new_marc_filename , 'wb') as data:
    for my_record in my_marc_records:
        data.write(my_record.as_marc())


```

We're not limited to a marc binary. PyMARC has a few options that we could use if we needed something else:

```python
data.write(my_record.as_dict())
data.write(my_record.as_json())
data.write(my_record.as_marc())
data.write(my_record.as_marc21())
```


{% include links.md %}