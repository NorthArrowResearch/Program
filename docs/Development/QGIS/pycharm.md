---
title: Debugging plugins using Pycharm
weight: 3
---

## Setting up pycharm to Autocomplete

When you use OSGEO4W to install QGis there are some libraries (notably QGis and Qt) that fall outside the usual python discovery paths. To get auto-completion to work for these you will need to add these paths manually.

1. In Pycharm: `Settings -> Project:YOURPROJECT -> Project Interpreter`
2. Click the Gear icon beside your project interpreter and choose the "More" Option 
3. Icon with little brown tree folders. When you hover it should say "Show paths for the selected interpreter"
4. Click the `+` button. 
5. Add 2 paths:
    * Windows: 
        * `C:\OSGeo4W64\apps\qgis\python`
        * `C:\OSGeo4W64\apps\qgis\python\plugins`
    * OSX
        * `/Applications/QGIS.app/Contents/Resources/python/`
        * `/Applications/QGIS.app/Contents/Resources/python/plugins/`

***NB: Depending on your install these files may be in a slightly different place***

-----------------

## Remotely Debugging QGIS applications in Pycharm

*The following will assume you have QGIS > 2.16 an the professional version of pycharm.* ***NB: the free version of PyCharm does not include a remote debugger***

### Pycharm Setup

In the `__init__.py` file there is a line of code to activate the `pydevd` server under certain conditions. We need to make sure Pycharm can find `pydevd` and then set an environment variable in QGis to trigger it.

#### 1. Add the debug eggs to the Pycharm project 

1. Pycharm `Settings -> Project:YOURPROJECT -> Project Structure`
2. Click `+ Add Content Root`
3. Find the Pycharm `debug-eggs` folder
    * OSX: `/Applications/PyCharm-app/Contents/debug-eggs`
    * Windows: ?????
4. Click `Apply` and close. 

#### 2. Create a remote debugger in Pycharm

1. Run -> Edit Configurations
2. `+` button then choose `Python Remote Debug`
3. Call it something like `QGIS Remote Debugger` and set host to `localhost` and port to `53100`
4. Click OK

Now you should be able to select the remote debugger from the `run` dropdown menu. This should show the following in the Pycharm terminal:

``` bash
Starting debug server at port 53100
Use the following code to connect to the debugger:
import pydevd
pydevd.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)
Waiting for process connection...
```

### QGis Setup

Now that we have a remote debugger we need to do one additional thing in QGis.

1. Load Qgis. Go to `Preferences -> System -> Environment`
2. Create a new variable called `ENVIRONMENT` with a value of `DEBUG`
3. Reload QGis and if you've got the Analyst Toolbar installed it should break in Pycharm when you load QGis. 

Click the play button in Pycharm to let QGIS load up the rest of the way and from now on it should break in pycharm at breakpoints you set.

---------------------

## More Resources:

* [Remote Debugging in PyCharm](https://www.jetbrains.com/help/pycharm/2016.1/remote-debugging.html)