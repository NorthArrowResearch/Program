---
title: Jekyll Toolbox
---

This page contains a suite of techniques for enhancing web sites stored on GitHub. GitHub uses [Jekyll](https://jekyllrb.com) to take a set of documents written in [markdown](https://en.wikipedia.org/wiki/Markdown) and publish them as a full blown web site. What follows are several tricks, techniques and patterns for enhancing these Jekyll web sites with features that make the web sites more useful. For example, adding a table of contents or injecting a page header.

## Front Matter

Each markdown document in your site should contain a small section at the top that is referred to as front matter. This section contains a series of tags and keywords that tell Jekyll a few things about the final web page. The most common and important tag is the `title` tag. Jekyll uses this to set the HTML page title for each document.

Front matter must occur at the very top of the markdown document and begins and ends with three hyphens. Inside the front matter is a series of keywords, followed by a colon, a space and then the value for the item. Note that the keyword, in this case `title`, **is case sensitive**! So setting the page title would look like: 

```
---
title: This Is My Page Title
---

Page content goes below....
```

## Site Table of Contents

