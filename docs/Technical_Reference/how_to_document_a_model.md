---
title: How to Document a Model
---

The information on this page is intended to help model owners through the steps of publishing their model and sharing it with the broader audience. This refers to uploading the source code, licensing the code and providing the supporting documentation. 

It is advisable that the steps below are performed in the order in which they are described. Some activities only make sense if the preceding tasks have been completed.

## Source Code Check List

Here are some things to remember before uploading your source code onto the internet. Review **all** the files in **all** the folders in your source code directory and:

* Ensure that all the files needed to run the source code are in the repo! The best way to confirm this is to copy the source code onto a separate computer that has never had the source code on it before and then try and run the code there. Guaranteed the first time you do this it will not work and you will realize that you've forgotten to include one or more files. External dependencies don't need to go in your repo, but any file that you've authored should be included.
* Delete any temporary files or files that are no longer needed.
* Remove sensitive information such as user names and passwords in any files. It's best that your code reads these from a configuration file that is separate from your source code. This configuration file can then be excluded from your repo using a [.gitignore](https://help.github.com/articles/ignoring-files/) file. If you do this, then it can be helpful to create another file called something like `config.TEMPLATE`, with the exact same structure as your configure file, but without the sensitive information, and then include this in the repo. Others trying to use your code can use this template as a starting point.
* Avoid putting binary files in your repo (databases, DLLs, compiled items etc). Again, use a [.gitignore](https://help.github.com/articles/ignoring-files/) file to exclude these.

## Source code in Riverscapes GitHub

Your source code should be stored in a git repository and uploaded into the [Riverscapes ](https://github.com/orgs/Riverscapes/dashboard) organization on GitHub. If you're new to GitHub, the default is to upload repositories under the umbrella of your own user account, so it's important that you understand how to upload the repo under the riverscapes organization.

You should learn and understand how to use git first! Certainly research any of the terms below that are not readily obvious to you. But, at a high level, starting from a folder of non-version controlled source code on your computer, the steps are:

1. Install git version control software. 
2. Initialize a new git repo in your top level source code folder.
3. Commit all changes to the git repo.
4. Login to [GitHub](http://github.com)
5. Navigate to the [Riverscapes organization](https://github.com/orgs/Riverscapes/dashboard).
6. Click the green **New Repository** Button and fill in the necessary fields.
7. Copy the SSH address that GitHub provides once the repo is created.
8. On your local system, add a new **Remote**. Call it `origin` and paste the SSH address.
9. Push your source code up to origin.
10. Refresh the repo page on GitHub and verify that your source code appears.



## Tag your releases

Review the commit history and create git [tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) at each official release using a systematic numbering system. Remember to **push** your tags to origin (or they will only reside on your local git repo).



## Read Me File

Add a file to the top level folder of your repo called `readme.md` The `md` suffix tells GitHub that this is a plain text [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) document. It's important because GitHub renders this readme file below the listing of source code. See the [bottom of the PyBRAT repo](https://github.com/Riverscapes/pyBRAT) for an example.

Learn [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) if you don't know it already. You're going to be writing a lot of it!

For now, simply put one or two sentences in the read me that provide a high level overview of your model. You will be adding more information to this file later...

## License File

Create and a plain text file in the root of your repository simply called `LICENSE` (no file suffix). [Choose an appropriate license](https://choosealicense.com/) and put the text in this file. Most Riverscapes models use the [GNU 3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Documentation Site

GitHub can build a web site for your model from simple text files stored in your repo! This is an excellent way to quickly and easily build a professional, polished documentation wiki for your model that users can read to learn more about how it works. The beauty of this approach is that all you need to write are simple text files using the [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax. No understanding of web technology is required! Here are a couple of examples:

* [PyBRAT](http://brat.riverscapes.xyz/)
* [RCAT](http://rcat.riverscapes.xyz/)

Here are the steps to create a documentation web site for your model:

1. Create a folder called `docs` in your local source code folder on your computer.
2. Create a file called `index.md` in this docs folder. This will become your web site home page.
3. Push your changes up to `origin` (i.e. the GitHub remote).
4. Open your repo home page on GitHub and:
   1. Click on the Settings link above the source code listing.
   2. Scroll down until you see **GitHub Pages**
   3. Choose **master branch /docs folder** in the source dropdown.
   4. Click **Save**.
   5. Wait 2-3 minutes for the site to get generated.
   6. Click on the link shown for your web site. Typically it will be of the form `http://riverscapes.github.io/YOURREPONAME`
5. Create whatever other web pages you need and also store them in the docs folder. You can use folders to separate and group files. Note that the folder names are going to be interpreted into links on the web site. So do **not** use spaces in folder names. Instead use underscores in place of spaces, and do use capitalization. File names are not used as links, but the informal standard is to also avoid spaces and use all lower case for file names.

You will need to wait 2-3 minutes after each push to GitHub for your site to be generated from your markdown documents.

### Site Content Recommendations

It's recommended that - at an absolute minimum - you cover the following topics in your web site:

* **Release Notes** - include a single page that lists each of the official releases, the date of the release, together with some high level description of the changes. Here's [an example](http://workbench.northarrowresearch.com/release_notes.html).
* **Acknowledgements** - content describing the contributors and funding sources.
* **Source Code** - link back to the GitHub repo so readers can easily obtain the source code should they need it.
* **Citations** - Either at the bottom of the home page, or on a dedicated page should more space be required.
* **Getting Started** - instructions on how users download, configure and run the code.
* **Prerequisites** - A list of dependencies required by users before the code will run, together with links and/or instructions on how to obtain them. This next point is incredibly important! It is often hard to know what technologies that you have on your computer are actually in use by your code. You should install your code on a *clean* computer that has never been used for development or had the source code on it to thoroughly understand what all is required. This is the only true way to understand what is required. Not doing this test will almost certainly mean that your instructions will be incomplete for some users that have a different computer configuration than you.