For using the web server 'cherrypy' must be installed.
1. Download Cherrypy from: http://www.cherrypy.org/wiki/CherryPyDownload
   or directly from: http://download.cherrypy.org/cherrypy/3.2.0/
2. Install it by extracting the package and running "python setup.py"
   in a shell (for linux systems).
   
   
Installing MySQL on Debian based systems:
run: apt-get install mysql-server mysql-client libmysqlclient15-dev
NOTE: it is important to install the libmysqlclient15-dev, else you could
      receive errors in the next step.

   
For running the setup, you will also need the MySQLdb driver.
NOTE: MySQL needs to be installed before running the installation for the following packages.
1. Install "python-setuptools" for your distribution. For Debian based systems
   use: apt-get install python-setuptools
2. Download the driver from http://sourceforge.net/projects/mysql-python/
3. Install it by extracting the package and running "python setup.py install"
   in a shell (for linux systems).