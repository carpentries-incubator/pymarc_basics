---
title: Introduction and Setup
teaching: 10
exercises: 15
objectives:
- Install and check Python v3.x
- Install and check pymarc
- Collect data files used in lesson
- Basic preflight checks 
keypoints:
- The software we need for the lesson is correct versions and works as expected
- The files we need for rest of lesson are available
---

## Episode 1: Getting Started

# Hello World!

Start a new python file in your IDE of choice. 

We're using SublimeText, so we just need to save a new file as test.py in SublimeText. 

We can get python to tell us what version it is with the following code:

```Python
import sys
print(sys.executable)
```

To 'deploy' the script in Sublime, you can use the following keystrokes:

<kbd>Control</kbd> + <kbd>S</kbd> to save your changes

<kbd>Control</kbd> + <kbd>B</kbd> to "build" the script and run it. 

Its worth remembering these two commands, you'll use them a lot in this lesson! 

We're looking to see where python is installed - theres a version number in the file path. 
We want to see <code>Python3x</code> to make sure we're all using Python version 3. 
 
<code>C:\Users\gattusoj\AppData\Local\Programs\Python\Python38\python.exe</code>

Next we need to install pymarc. 

Open command line by hitting the <kbd>Windows</kbd> key, type <code>cmd</code> and hit <kbd>Enter</kbd>  
Open terminal if you're on Linux - <kbd>Ctrl</kbd>+<kbd>t</kbd>

To install packages, we use a tool called 'Pip Installs Packages' or better known as PIP. To install pymarc, at the cursor type <code>pip3 install pymarc</code> and hit <kbd>Enter</kbd>. You need to be connected to the public internet to use PIP. 
If it worked, you should see something like:
<code>Successfully installed pymarc-3.2.0</code>

Make a folder to hold all the files we'll use in this lesson called <code>pymarc_basics</code> somewhere that you can easily find. 

To test it worked, open your IDE (SublimeText) and make a new python file (e.g. <code>test.py</code>) and type:

```Python
import pymarc

print ("{}".format("Hello World!") 
```

Run the script, and if there is no error messages in the python terminal window and you see the text <code>Hello World!</code>, you've successfully installed pymarc! 

We're using a slightly over complicated way of printing our "Hello World!" string in this test. There a subtle but important difference in some versions of Python, and how it handles text. By using this <code>format()</code> method we can double check that we're using a version of Python that will work OK with the rest of the lesson.  

We need to make sure we have a local copy of the MARC file we'll use for the rest of the lesson. You can find all the data files, and helper scripts in the setup folder: [http://bit.ly/2PItN0Y](http://bit.ly/2PItN0Y)

At minimum, download the <code>NLNZ_example_marc.marc</code> file. There are other <code>.marc</code> files in that location. These just contain more records. Download them if you want to have more MARC records to explore. 

Save any MARC files in to the same folder as your scripts. 

You should have a folder structure that looks like this:

```
pymarc_basics
	episode_1.py
	test.py
	NLNZ_example_marc.marc
	...
```

# Hello PyMARC! 

Finally, lets put all this together, and see if we can read the marc file. 

Start a new python file, <code>episode_1.py</code> and type the following code:

```Python
import pymarc

my_marc_file = "NLNZ_example_marc.marc"

with open(my_marc_file, 'rb') as data:
	reader = pymarc.MARCReader(data)
	for record in reader:
		print (record.title())
```


We'll cover off this script in the next episode. For now you want to see a list of titles that are included in our test set of MARC records:
```
Larger than life : the story of Eric Baume /
Difficult country : an informal history of Murchison /
These fortunate isles : some Russian perceptions of New Zealand in the nineteenth and early twentieth centuries /
As high as the hills : the centennial history of Picton /
Revised establishment plan.
A Statistical profile of young women /
Chilton Saint James : a celebration of 75 years, 1918-1993 /
Tatum, a celebration : 50 years of Tatum Park /
The Discussion document of the Working Party on Fire Service Levy / ... prepared by the Working Party on the Fire Service Levy.
1991 New Zealand census of population and dwellings.
```

{% include links.md %}