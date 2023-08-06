import os
import re
from setuptools import setup

_long_description = """
### How to import the Rubik's library

``` bash
from libraryArsein.Arsein import Robot_Rubika
```

### How to install the library

``` bash
pip install ArseinRubika==4.6.1
```

### My ID in Telegram

``` bash
@Team_Arsein
```

## An example:
``` python
from libraryArsein.Arsein import Robot_Rubika

bot = Robot_Rubika("Your Auth Account")

gap = "your guid or gap or pv or channel"

bot.sendMessage(gap,"libraryArsein")
```
Made by Team ArianBot

Address of our team's GitHub :

https://github.com/Arseinlibrary/Arsein__library.git
"""

setup(
    name = "ArseinRubika",
    version = "4.6.1",
    author = "arian abasi nedamane",
    author_email = "aryongram@gmail.com",
    description = (" library Robot Rubika"),
    license = "MIT",
    keywords = ["rubika","bot","robot","library","rubikalib","rubikalib.ml","rubikalib.ir","rubika.ir","libraryArsein","libraryarsein","Rubika","Python","libraryArseinRubika"],
    url = "https://github.com/Arseinlibrary/Arsein__library.git",
    packages=['libraryArsein'],
    long_description=_long_description,
    long_description_content_type = 'text/markdown',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
    ],
)
