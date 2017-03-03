---
title: Writing & Validation XML
weight: 2
---

When your tools write XML files

## When to Validate?

XML validation is useful for making sure the XML files your tool is outputting are valid and will work with the rest of the system. You don't need to validate every time the tool creates an XML though. Generally you should only have to validate during tool development before you publish a version of the tool to make sure the XML it is producing is ok.

## Validating XML (in Pycharm):

In addition to being a great Python IDE, PyCharm also has an excellent XML editor built-in.

Validating an XML file is almost automatic in pycharm but first you have to make sure the XML file you're looking at can find the schema it needs:

### Make sure you have a good XSD reference:

Look at the first two lines of the xml you should see something like:

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="XSD/V1/Project.xsd">
```

This file is looking for a local `Project.xsd` in a folder `XSD/V1` relative to where this XML file is located. You can do one of 2 things here:

1. Move this XML file to a place that can find  `./XSD/V1/Project.xsd` 
2. Change the Address to something else (like a web url)

**NorthArrowResearch is currently hosting the current version of the project XSD here:**

* **Development**: `https://raw.githubusercontent.com/Riverscapes/Program/master/Project/XSD/V1/Project.xsd`

**Note**: The development URL is in github and may change over time (both the url AND the contents of the file). The production url will increment the version so `V1` will always be Version 1 etc.  

So if you just change the top line to:

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Riverscapes/Program/master/Project/XSD/V1/Project.xsd">
```

#### Pycharm Caveat: Add remote URLs

You will notice (in Pycharm) that the address turns red and causes an error. If you hover over it you will see a red lightbulb indicating an [intention action](https://www.jetbrains.com/help/pycharm/2016.2/intention-actions.html). One of the choices it will give you is "**Fetch external resource**". Once you do that you will see autocomplete working just fine.

**Further Reading:** 

* [Referencing XML Schemas and DTDs](https://www.jetbrains.com/help/pycharm/2016.2/referencing-xml-schemas-and-dtds.html)
* [Pycharm Intention Actions](https://www.jetbrains.com/help/pycharm/2016.2/intention-actions.html)

----------------------------

#### Pycharm: Quick Vs. Full Validation

Quick validation happens automatically. Things like unclosed tags, invalid tags etc. will be caught as you type. 

Full validation will catch more nuanced errors like elements out of order and unlawful elements duplication. It has to be done manually and there are two ways to do this:

1. Right-click anywhere in the document and choose `Validate`.
2. In the menus choose: `Tools -> XML Actions -> Validate`

This will cause your XML file to be validated against the XSD file that is hopefully located in the same directory.

It is recommended that you validate fully before each git commit.