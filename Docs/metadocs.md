---
title: "Meta docs: How to use this wiki"
menu: "mainMenu"
---

[Hugo](https://gohugo.io/) provides an easy-to-use, secure, easily-deployable document management system. It works using markdown for everything.

**Markdown:** There's a great cheat sheet for Markdown [here](http://scottboms.com/downloads/documentation/markdown_cheatsheet.pdf).

### Workflow for editors:

1. Pull the repo
2. Edit the repo (create files, edit files etc.)
3. Commit the change
4. Push the change (this will deploy it)

### Making changes.

Any of the files with a `.md` extension can be edited

Once you are done, save the file. If you switch to your github app you will notice some uncommitted changes. Make sure your changes have a checkbox that is checked, enter a short summary note like "updated the translation page" and click `commit`.

Committing is only a local function. To publish your changes on the server you need to "push" or "sync" them. The github app has a `sync` button in the to right. Changes should apeear live on the site within a few seconds of syncing.

### Adding new Docs

All you need to do is create a new file somewhere in the directory structure (please help us keep this organized) and call it something like `doc-name.md`. The filename will only appear in the url bar.

Now open this file and add the frontmatter. [Frontmatter](https://gohugo.io/content/front-matter/) is a few lines at the top of the file that tells this document how to display to the user:

Here is an example for pages:

~~~bash
---
title: Translation of PSAC content
---
~~~

Here is an example for meeting minutes:

~~~bash
----
title: NSF Status Meeting
date:   2014-04-07
author: Philip
---
~~~


*NB: if your title is breaking it might be because it has special characters. This can be fixed by "Putting your title in quotations".*


## Images

~~~bash
![This is an image](/images/logo.png)
~~~

![This is an image](/images/logo.png)

## Tables

Tables in markdown are a little ugly. There are tools to help you with them like [tablesgenerator.com](http://www.tablesgenerator.com/markdown_tables).

**Doing:**

~~~bash
Name    | Age | City      | Fav Animal
--------|-----|-----------|-----------
Bob     | 27  | Vancouver | skybison
Alice   | 23  | Toronto   | molerat
~~~

**Will Give you:**

Name    | Age | City      | Fav Animal
--------|-----|-----------|-----------
Bob     | 27  | Vancouver | skybison
Alice   | 23  | Toronto   | molerat


#### Simple Code Blocks

If your code isn't any particular language you can use 3 backticks: before and after it. to get a nice code block.

#### Code Color Highlighting

Hugo does code highlighting in a really straightforward way: by enclosing your code in tildes plus the name of the language

So if I do this:

~~~php
~~~php
<?php 
  //Put your code here
  $colors = array("red","green","blue","yellow"); 

  foreach ($colors as $value) {
    echo "$value <br>";
  }
?>
\~~~
~~~

I will get this:

~~~php
<?php 
  //Put your code here
  $colors = array("red","green","blue","yellow"); 

  foreach ($colors as $value) {
    echo "$value <br>";
  }
?>
~~~

More about how code highlighting works [here *(bottom of the page)*](https://gohugo.io/extras/highlighting/).
