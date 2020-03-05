---
title: Saving MARC Files
teaching: 15
exercises: 30
objectives:
- How to save MARC records
keypoints:
- We can save a MARC record to a suitable format
- We can save MARC records to a suitable format 
---
Episode 6: Saving MARC Files pymarc

Start a new file in your IDE <code>episode_6.py</code>

Set up the basic record reader like we have previously, this time we're only going to process one record: 

```python
from pymarc import MARCReader
my_marc_file = "NLNZ_example_marc.marc"


with open(my_marc_file, 'rb') as data:
    reader = MARCReader(data)

```


{% include links.md %}