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

#### 1. Create a remote debugger in Pycharm

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



#### 2. Create a launcher for QGIS

In order to run QGIS with the remote debugging eggs you need to launch it with the following:

##### `QGIS-debugenv.cmd`

```Bash
@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
set PYTHONPATH=%PYTHONPATH%;c:\Program Files\JetBrains\PyCharm 2017.1.2\debug-eggs\pycharm-debug.egg
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

rem EVERYTHING FROM HERE DOWN IS TAKEN FROM THE `qgis.bat` file

set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt4\plugins
start "QGIS" /B "%OSGEO4W_ROOT%"\bin\qgis-bin.exe %*
```

### QGis Setup

Now that we have a remote debugger we need to do one additional thing in QGis. Launch it with the new launcher you created.

1. Load Qgis. Go to `Preferences -> System -> Environment`
2. Create a new variable called `DEBUG_PLUGIN` with a value of `RiverscapesToolbar`
3. Reload QGis and if you've got the Analyst Toolbar installed it should break in Pycharm when you load QGis. 

Click the play button in Pycharm to let QGIS load up the rest of the way and from now on it should break in pycharm at breakpoints you set.

-----------

## Setting up your plugin for remote debugging

What are we trying to achieve here?

* A `DEBUG` flag we can use throughout the code to wall-off things we don't want to run in production
* Making sure we only try to connect to a debug server if we are:
  1. In dev mode
  2. Specifically debuggin this one plugin



**There are lots of options here but this is how I do it:**

#### 1. create a module called `debug.py`

```Python
import os

######################### REMOTE DEBUG #########################
def InitDebug():
    if 'DEBUG_PLUGIN' in os.environ and os.environ['DEBUG_PLUGIN'] == "RiverscapesToolbar":
        import pydevd
        pydevd.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True, suspend=False)
######################### /REMOTE DEBUG #########################
```

#### 2. Link to it from your `__init__.py`

Now in your project's `__init__.py` add the following:

```Python
######################### REMOTE DEBUG #########################
# To activate remote debugging set DEBUG_PLUGIN=RiverscapesToolbar as a QGIS
# Environment variable in Preferences -> System -> Environment
import os
import logging
DEBUG = False

from RiverscapesToolbar.lib import debug
if 'DEBUG_PLUGIN' in os.environ and os.environ['DEBUG_PLUGIN'] == "RiverscapesToolbar":
    debug.InitDebug()
    DEBUG = True
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
######################### /REMOTE DEBUG #########################
```

Note that some paths will likely need to be changed. `debug` module may not live at `RiverscapesToolbar.lib` 



---------------------

## More Resources:

* [Remote Debugging in PyCharm](https://www.jetbrains.com/help/pycharm/2016.1/remote-debugging.html)