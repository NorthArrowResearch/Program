---
title: QGIS Installation (Dev Windows)
weight: 1
---

If you're not a developer just [download an install QGIS normally using the standalone installer](http://www.qgis.org/en/site/forusers/download.html). However, there are several important components that are needed for QGIS plugin development, and developers should follow the instructions below:

## Install OSGeo4W64 (Windows only)

[OSGeo](http://www.osgeo.org/) is a bundle of several open source GIS components that includes QGIS. The installer has a user interface for selecting which components that you want to install.

Go and get the OSGeo installer from the [QGIS download site](http://www.qgis.org/en/site/forusers/download.html). It's listed underneath the standalone installers. Choose the 64-bit version if you have a 64 bit version of Windows.

1. Double click the OSGeo setup exe file to start the installation.
2. Make sure to select `Advanced Install`.
3. Choose `Install from Internet`
4. When selecting the root directory you need to type `C:\` before the suggested root directory. The root directory should look like `C:\OSGeo4W64`. You can leave the `all users` option enabled.
5. Accept the `local package` and `start menu` name suggestions.
6. Leave the `direct connection` option enabled.
7. Single click on the one and only available download site.
8. **Important** choose to install the following packages:
 * `Desktop -> qgis`: QGIS Desktop
 * `Libs -> python-scipy` (not needed for anything but nice to have)
 * `Libs -> qt4-devel` (needed for lrelease/translations)
 * `Libs -> setuptools` (needed for installing pip)
9. Accept the remaining screens...

### Create 2 `.cmd` files

The OSGeo suite of tools, including QGIS, are designed to be multi-platform. To achieve this, it means that these tools cannot use some of the Windows-specific software installation techniques. This manifests in some behaviours that can be unfamiliar to Windows users. For example, Windows users do not launch QGIS simply by clicking on the software executable. Instead, a small batch file is used to launch QGIS. This batch file configures all the necessary environment settings needed to help the suite of OSGeo tools find dependencies and libraries. The following instructions resuse and extend these batch files to make things a little easier:

#### `console-qgisenv.cmd`

The first file  you will create is a straight-up environment file for using the OSGeo4W console. This is essentially a DOS prompt that is aware of all the OSGeo tools and that you can use for performing command line operations. e.g. Python or GDAL operations.

Copy and paste the following text into a new file and save it somewhere convenient, `C:\OSGeo4W64` is a logical choice, although remember that this will get deleted when you remove OSGeo and require you to recreate it next time you install:

``` sh
@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

cmd.exe
```

#### `pycharm-qgisenv.cmd`

The second file will be used to launch [PyCharm](https://www.jetbrains.com/pycharm) in the context of QGIS. This is extremely important. It will allow your PyCharm sessions to find and use the same version of Python that QGIS uses, and also debug plugins that are running within a QGIS session.

``` sh
@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
start "PyCharm aware of Quantum GIS" /B "C:\Program Files (x86)\JetBrains\PyCharm 3.4.1\bin\pycharm.exe" %*
```

***NB: Be sure to check the 2 paths on your local system that may be different based on where you chose to install OSGeo and PyCharm:***

* `C:\OSGeo4W64` -- Wherever you installed OSGeo4W
* `C:\Program Files (x86)\JetBrains\PyCharm 3.4.1\bin\pycharm.exe` -- Note the version number in the path. Regrettable. 

### Testing and Install Dependencies

The following are a couple of tests that should be performed to make sure that OSGeo, Python, QGIS and PyCharm are all installed correctly and can find each other:

Double click `pyqgis-console.cmd` and type the following

``` sh 
c:\> python
```

Now you have a python console you can test things in (and that you know is the same version of Python that your installation of QGIS is running).

``` python
Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

At the Python prompt (`>>>`) type the following:

``` python
>>> import qgis.core
>>>
```

If it doesn't complain after you type `import qgis.core` then you're good to go.

Exit the Python prompt (`CTRL Z`) and now type:

``` bash
c:\> easy_install pip
```

This installs [pip](https://pypi.python.org/pypi), which is the Python packaging tool. Pip maintains an index of official Python pacakages (e.g. SciPy) and help's you install them with a single command.

Finally, type the following at the DOS command prompt: 

```
c:\> pip install pb_tool
```

This installs the [QGIS Python plugin development](https://pypi.python.org/pypi/pb_tool/1.9) package needed to develop QGIS plugins. Now you have everything you need to compile and debug QGIS plguins in pycharm. You will need to read the page called [Debugging plugins using Pycharm]({{site.baseurl}}/Development/QGIS/pycharm/) to set that up. 
