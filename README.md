Alfred 2 Workflow for Prowl
====================

This [Alfred 2 workflow](http://www.alfredapp.com/) allow you to send Prowl alerts to your mobile phone. 

For information on how to install and use this workflow, please visit the [Prowl for Alfred](http://ken.pepple.info/prowl.alfredworkflow) homepage.

Requirements
------------

This workflow requires [Alfred 2 and the Powerpack](http://www.alfredapp.com/powerpack/) and [Prowl](http://www.prowlapp.com/).

Code Structure
--------------

There are three important code files:

* The `info.plist` is the control file required by Alfred. It has the bare minimum of code to start the prowl commands.
* The `prowl_alfred.py` is the main code file. It sets configuration options, verifies Prowl API keys and send Prowl notifications.  
* The `alfred_utils.py` contains some helper methods to read/write config files

This workflow uses the [Python Requests](http://docs.python-requests.org/en/latest/) library to make API calls. It is embedded in the workflow to ease installation.

The Prowl API is defined at [http://www.prowlapp.com/api.php](http://www.prowlapp.com/api.php).

Configuration Files
-------------------

There is a single configuration file:

* config.ini

This file follows the standard ini format. The only option is "apikey". A sample would look like this:

```ini
[defaults]
apikey = b57501d2e56cfd64316153da47355283db4752fc

```

This shouldn't be set by hand - rather the cmd modifier will set it for you.

Alleyoop Support
----------------

This workflow supports [Alleyoop](http://alfred.daniel.sh/oopdev.html) through its remote.json and update.json files. 

