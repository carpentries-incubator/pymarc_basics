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

Let set up a 



{% include links.md %}