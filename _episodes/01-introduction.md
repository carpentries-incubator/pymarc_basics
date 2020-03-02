---
title: Introduction and Setup
teaching: 0
exercises: 0
objectives:
- Install and check Python v3.x
- Install and check pymarc
- Collect data files used in lesson
- Basic preflight checks 
---
Episode 1: Getting Started


#Pre-Requirements

The first thing we need to do is make sure we can use Python, and we're all using the correct version of Python. 

If you've not installed python yet, please install the latest version (https://www.python.org/downloads/)

If  you don't have an Interactive Deployment Environment (IDE) install Sublime text v3 (https://www.sublimetext.com/3) N.B. If you laptop has corporate controls/permission, try the portable version. 

# Hello World!

Start a new python file in your IDE of choice. 

We're using Sublime Text, so we just need to save a new file as test.py in SublimeText. 

We can get python to tell us what version it is with the following code:

```Python
import sys
print(sys.executable)
```

We're looking to see where python is installed - theres a version number in the file path. 
We want to see <code>Python3x</code> to make sure we're all using Python version 3. 
 
<code>C:\Users\gattusoj\AppData\Local\Programs\Python\Python38\python.exe</code>

Next we need to install pymarc. 

Open command line by hitting the <kbd>Windows</kbd> key, type <code>cmd</code> and hit <kbd>Enter</kbd>  
Open terminal if you're on Linux - <kbd>Ctrl</kbd>+<kbd>t</kbd>

To install packages, we use a tool called 'Pip Installs Packages' or better known as PIP. To install pymarc, at the cursor type <code>pip3 install pymarc</code> and hit <kbd>Enter</kbd>. You need to be connected to the public internet to use PIP. 
If it worked, you should see something like:
<code>Successfully installed pymarc-3.2.0</code>

To test it worked, open your IDE (SublimeText) and make a new python file (e.g. <code>test.py</code>) and type:

```Python
import pymarc

print ("Hello World!") 
```

Run the script, and if there is no error messages in the python terminal window and you see the text <code>Hello World!</code>, you've successfully installed pymarc! 

We need to make sure we have a local copy of the MARC file we'll use for the rest of the lesson. # todo [make this easier to grab the binary] https://github.com/jayGattusoNLNZ/pymarc_basics/blob/gh-pages/files/NLNZ_example_marc.marc and download the <code>NLNZ_example_marc.marc</code> file.

Save it in the same folder as your scripts. 

# Hello PyMARC! 

Finally, lets put all this together, and see if we can read the marc file. 

Start a new python file, <code>episode_1.py</code> and type the following code:

```Python
import pymarc

my_marc_file = "NLNZ_example_marc.marc"

reader = pymarc.MARCReader(open(my_marc_file, 'rb'), force_utf8="True") 

for record in reader:
    print (record['245'])
```

We'll cover off this script in the next episode. For now you want to see a list of titles that are included in our test set of MARC records:
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