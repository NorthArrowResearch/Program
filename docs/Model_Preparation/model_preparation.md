---
title: Model Preparation
---

We are building a warehouse to store model results that directly and indirectly feed into the calculation of fish capacity and life cycle modelling. Ostensibly this is for [CHaMP](http://champmonitoring.org), but we intend to reuse what we learn during this process and pioneer a strategy for organizing *any* hierarchical spatial data.

Within CHaMP there are numerous *models*, by which we mean any tool, software, script, formula that transforms data. A model takes one or more input datasets, manipulates them in some way, and produces one or more outputs. Using the [Geomorphic Change Detection](http://gcd.joewheaton.org/) (GCD) software as an example, the most basic inputs would be two DEMs, the transformation a raster subtraction and the output a new raster representing the change.

There are other types of models and they can take many forms. A simple script that copies the values in the attribute fields from several ShapeFiles onto a single ShapeFile can be considered a model. Essentially, **a model is any process that alters data**.

To take this one step further, the collection of a single set of model inputs and their corresponding outputs we are calling a **project**. Reusing the GCD example, a GCD project consists of two DEM rasters, some intermediate datasets, and then the output DoD raster. These project items are organized on a computer in a consistent **file and folder hierarchy** and the paths to each dataset described in a **project file**. The project file also stores useful metadata (who ran the model, when, and what version of the software was used) as well as model specific results (the GCD project file stores the volume of erosion etc).

The final piece of this puzzle is that for users to view model results we need to know how to display the contents of a project. This involves two things: 1) defining how to organize the inputs and outputs as layers in a GIS table of contents, and 2) how to symbolize these same layers. We are calling the combination of these definitions the "business logic" because it is less about the technical task of storing files and more about how end users will interact with the model results during analysis, review etc. Essentially working with the data.

In summary, we are building a sizable file and folder store to house all the model projects in one **data warehouse**. This is a fancy term for a big hard drive of well-organized model inputs, outputs, project files and other useful context layers (aerial imagery, hillshade etc). The warehouse will be maintained in the cloud (Amazon Web Services) and we are building tools to view, download, upload and work with the contents. 

To help move this effort forward we need to define each model, it's project file and folder structure and the accompanying business logic. For each model we need to define:

1. Phase one
	1. file and folder hierarchy
	1. GIS table of contents hierarchy
	1. GIS table of contents symbology
1. Phase two
	1. Project file structure
	1. Business logic structure

Your mission - should you choose to accept it - is to help us with Phase one. Here are the tasks:

# Tasks

Complete each of the tasks below. Each task ends with deliverables that need to be provided. Read to the bottom for instructions on how to bundle all the deliverables and send them to the developers as well as the schedule for completion.

## 1. Model Identification

a. Provide the full name of your model (e.g. "Geomorphic Change Detection")

b. Provide the abbreviated name of your model (e.g. "GCD")

c. Web site URL (if the model has an existing home online)

The full name will be used in reports and potentially user interface design (if there's enough screen real estate). The abbreviated name will be used for folder names (and other places where there are limitations in the number of characters available).

**Deliverables**:

1. Model full name
1. Model abbreviated name
1. Web site URL

## 2. Organize Files and Folders

Take the entire set of files for a single model run. This will represent a "project" for your model. Note that there might be many simulations or calculations within the project, but the project represents the unit at which you will upload and download your model results. Typically this coincides with the level at which all the inputs are the same. Using the GCD example once again, a CHaMP GCD project represents a site and contains all the DEMs captured at each visit. The GCD project contains multiple DoD results.

So your task is to design the folder and file structure for your model for a single project. You should literally create the folders and files on your computer! If you don't have an existing model run on-hand then create fake examples of all the files necessary.

Think ahead, and include items that you might not have on hand, but know that you will need in the future. Include EVERYTHING related to the project! plots, rasters, images, metadata, CSV files, hyperlinks, PDFs, result tables etc. If any of the files are too big, just create a simple text file but rename it with the desired file name (see next step).

**Deliverables:**

1. Project folder with example file and folder structure.

## 3. Document Project File and Folder Structure

We need you to describe/document the file and folder structure that you just created. We have created a template that you should fill in. It contains one blank worksheet for you to populate and one sheet with the example of the GCD already filled out.

Steps:

1. Open the template Google Sheet that Philip shared with you.
1. **Make a copy!** including your model name in the name of the new Google Sheet.
1. Read the cell comments on row 11 to understand what values to fill in.
1. Fill in the contents, describing your model
1. **Share** your new sheet with edit privileges to:

`philip@northarrowresearch.com,matt@northarrowresearch.com,joe.m.wheaton@gmail.com,wally.macfarlane@gmail.com,jtgilbert89@gmail.com
`

Don't worry if you don't fully understand all the terms. And don't worry if feel torn because you want to organize things in different ways. This is the beauty of the business logic concept. We can have a single file/folder structure that is displayed using multiple different representations. If this is the case, then add worksheets to the Google Sheet with multiple hierarchy definitions.

**Deliverables:**

1. Spreadsheet describing the project files and folders. Use columns to represent nested folders and rows for each item. See the GCD example sheet.


## 4. Create ArcMap Document

Create an ArcMap `*.mxd` file in the same folder as the example project that you created above. Load all the data from the example project created above. Use group layers and sub-group layers to layout the envisioned logic of the tree (matching business logic structure above, but with more descriptive labels). The ArcMap table of contents should loosely represent the folder structure, but they can deviate if needed.

Make sure that you turn on [relative paths](http://resources.arcgis.com/en/help/main/10.1/index.html#/Referencing_data_in_the_map/00660000000w000000/) in the map document.

**Deliverable:**

1. ArcMap map document saved to the same folder as the example project.

## 5. Symbolization

Symbolize all the layers in the ArcMap map document and order everything like you want it (note that order off groups for display purposes may be slightly different than order of the files and folders). Make sure that you use the correct layer classification (stretched, binned etc). And make sure that you consider the range of possible dataset values not just the example project files that you are using to demonsrate the concept. 

If the symbology is complicated or nuanced, then consider writing it down using words. Save the file in the project folder and communicate this to the developers.

1. ArcMap map document with all layers organized and symbolized. Save the map document again to ensure that the symbology is updated. 

## 6. Icons

Provide a model logo graphic and individual icons (if you have them) for different node types. Conceptual collections should generally be folders, but specific instances may be something cutesie (e.g. a DEM or network, etc.). These can be graphics of any dimension or file type. Save them to the project folder with appropriate names.

## 7. Additional Information

If you have any additional information, remarks, comments or notes that you think that the developers might benefit from when reviewing your work please place it in a file called `readme.txt` in the example project folder (next to the the map MXD document).

## 8. Delivery

Zip up the example project folder. This should contain the sample file and folder structure, the ArcMap MXD file, icons, readme files etc. Review the file size; if it's grater than 100Mb then consider removing large files and replacing them with placeholder text files.

Email the zip file or put it in Box, DropBox etc and send the link to `philip@northarrowresearch.com, matt@northarrowresearch.com, joe.m.wheaton@gmail.com, wally.macfarlane@gmail.com, jtgilbert89@gmail.com`

# Schedule

These tasks need to be completed no later than Friday 21st October. Philip Bailey and Matt Reimer will be in Logan on 24-26 October for a workshop where we will review the deliverables and then take this process to the next phase!

Email Philip if you have any questions.

