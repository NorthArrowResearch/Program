---
title: Theming a Jekyll Site
---

We have developed a single theme that controls the look and feel of sites related to riverscapes. It's the theme that's applied to this site. If you have a Riverscapes site that doesn't look like this page or is missing page elements used on this site, then you need to follow the instructions below.

These instructions describe how to apply this theme to both a new site, or update the theme for an existing site. The steps are manual and somewhat fiddly. Remember to review your changes in git before commiting them. You can always [run Jekyll locally](jekyll_toolbox.html#running-jekyll-locally) to ensure that your changes have not broken the site.

## Before You Start

You are going to need a copy of the Riverscapes **TemplateDocs** repo. You can either use the green `Clone or Download` button on the [repo's GitHub web page](https://github.com/Riverscapes/TemplateDocs), or you can use git to clone down the repo. Regardless, make sure that you have the **latest version**. This theme will change from time to time.

Now you are ready to apply the theme to your site. Choose the section below that applies to you. If your site has never had the Riverscapes theme applied to it before, then choose [Theming a New Site](#theming-a-new-site). If your site has some past version of the Theme applied, or you're unsure if it's up to date, then jump to the [Updating a Site That's Already Themed](#updating-a-site-thats-already-themed) section.


## Theming a New Site

1. Review your site. This might be in the root of your repo or in a subfolder called `docs`, it doesn't matter.
	1. Ensure that you have a home page called `index.md` in the root folder of your site.
	1. Check that all your markdown files have [front matter](jekyll_toolbox.html#front-matter) title tags.
	1. Check that all the images for your site are in a top level folder called `assets` and then a folder called `images`.
1. Copy the following files and folders from TemplateDocs and place them in the same location in your site:
    * `\assets\css`
    * `\assets\fonts`
    * `\assets\js`
    * `\src`
    * `\_config.yml`
1. Edit the _config.yml file and set the following:
    * Put the name of your site after `title`
    * Put a one sentence description on it's own line after `description`
    * If you're using a web address other than the GitHub pages IO address then put the root URL of your site after `url`.
    * If you are using the default GitHub pages IO web address for your site then put the name of your repo in `baseurl`
1. See the Updating your favicon section below.



## Updating a Site That's Already Themed

Sometimes we may make changes to the theme. These could be cosmetic or functional changes. If you've customized your CSS or Javascript then you are repsonsible for merging changes yourself. These instructions only apply to a fresh site or one where the CSS, Javascript and Jekyll templates haven't been customized.

1. Copy the following files from the Templatedocs repo into your repo/docs folder:
	* `assets\css\app.css`
	* `assets\css\app.css.map`
	* `assets\js\dist.js`
	* `assets\fonts\*`
	* `src\_includes`
	* `src\_layouts\default.html`
1. Compare your `_config.yml` file with the one in TemplateDocs and look for any changes. You could copy across the one from TemplateDocs, but be sure to rename your existing `_config/yml` file first because you're going to want to retain key information that you've already put in this file (site name, url, base url etc).
1. See the Updating your favicon section below.


## Updating your favicon

Favicons are little graphics that web browsers display on the browser tab beside the site title:

![favicon](/assets/images/favicon_demo.png)

Favicons used to be simple. Things have gotten more complicated, what with all the various devices and resolutions on which people could be viewing your site. Here's how you generate your own:

1. Find a nice sized copy of your logo that is square. A high quality image is most important, but also try to avoid images greater than 500 pixels across to avoid image distortion.
1. Go to a service like <http://www.favicon-generator.org> and upload your icon. It will generate lots images in various sizes. Put these files in the folder `assets/images/favicons`.
1. Open src/_layouts/default.html and add the following lines. Be really careful about the paths! Too many broken links and it starts to affect your google ranking.

```
<link rel="apple-touch-icon" sizes="57x57" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="{{ site.baseurl }}/assets/images/favicons/apple-icon-180x180.png">
<link rel="icon" type="image/png" sizes="192x192"  href="{{ site.baseurl }}/assets/images/favicons/android-icon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="{{ site.baseurl }}/assets/images/favicons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="96x96" href="{{ site.baseurl }}/assets/images/favicons/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="16x16" href="{{ site.baseurl }}/assets/images/favicons/favicon-16x16.png">
<link rel="manifest" href="{{ site.baseurl }}/assets/images/favicons/manifest.json">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="{{ site.baseurl }}/assets/images/favicons/ms-icon-144x144.png">
<meta name="theme-color" content="#ffffff">
```