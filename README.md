WSNServer
========

This collection of python scripts is useful for translating commands in a heterogenous 
network of various Wireless Sensor Nodes. You can define your general language and 
with dictionaries it sends localized commands to the node.
And well, it is also a general RESTful web applicance for accessing nodes in general.

Installation
------------

First you need to install [GIT](http://git-scm.com/) on your local host which is connected to the controlling node.
If you use Debian: `apt-get install git`

Afterwards you get the rolling-release version with:
`git clone git@github.com:Phialo/wsnserver.git`

For using the web server 'cherrypy' must be installed.
Download [Cherrypy](http://www.cherrypy.org/wiki/CherryPyDownload) and
install it by extracting the package and running `python setup.py`
   
You can use the sqlite database(not recommended due to lacking support of simultanous access) or 
install MySQL.   

Installing MySQL on Debian based systems:
`apt-get install mysql-server mysql-client libmysqlclient15-dev`

**NOTE:** it is important to install the libmysqlclient15-dev, else you could
      receive errors in the next step.

   
For running the setup, you will also need the MySQLdb driver.
**NOTE:** MySQL needs to be installed before running the installation for the following packages.

1. Install *python-setuptools* for your distribution. For Debian based systems `apt-get install python-setuptools`
2. [Download](http://sourceforge.net/projects/mysql-python/) the driver
3. Install it by extracting the package and running `python setup.py install` from the wsnserver directory


Usage
------


For running the translator you need a local Wireless Sensor Node. The development was done on a 
Renesas ZMD28-BRD.

Run:
`python SerialReader.py -h` for explanation of command line variables and use the source for further adjustment.

Very Boring legal stuff
------------------

Copyright (c) 2012, Bartholomäus Dedersen, Kamil Wozniak

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Supporters
---------

[Gooze](http://www.gooze.eu) - High quality cryptographic tools for GNU/Linux, Mac OS X and Windows
