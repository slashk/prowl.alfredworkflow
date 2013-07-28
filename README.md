Alfred 2 Workflow for Prowl
====================

This [Alfred 2 workflow](http://www.alfredapp.com/) allow you to send [Prowl](http://www.prowlapp.com/) alerts to your mobile phone. 

For information on how to install and use this workflow, please visit the [Prowl for Alfred](http://ken.pepple.info/prowl.alfredworkflow) homepage.

License
-------

This workflow is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

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

* `config.ini` which is located in `~/Library/Application\ Support/Alfred\ 2/Workflow\ Data/info.pepple.prowl/config.ini`

This file follows the standard ini format. The only option is "apikey". A sample would look like this:

```ini
[defaults]
apikey = b59991d2e56cfd64216153da47355283db4999fc
```

This shouldn't be set by hand - rather the cmd modifier option will set it for you.

Build Script
------------

The `make_workflow.sh` bash shell script builds the workflow by zip'ing the appropriate files.

Alleyoop Support
----------------

This workflow supports [Alleyoop](http://alfred.daniel.sh/oopdev.html) through its `remote.json` and `update.json` files. 

