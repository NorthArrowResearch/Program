---
title: How to Document a Model
---

The information on this page is intended to guide model owners through the steps of publishing their model. In this context, publishing refers to uploading the source code, licensing the code and providing the necessary documentation. This is more about housekeeping and making your model accessible to others than any specific software development activity. 

It is advisable that the steps below are performed in order as some activities only make sense if the preceding task has been completed.

## Source Code Check List

Here are some things to remember before uploading your code onto the internet. Review all the files in all the folders in your source code directory and:

* Make sure all the files needed to run the source code are in the folder! The best way to copy the source code folder onto a separate computer that has never had the source code on it before and try and run the code there. Guaranteed the first time you do this it will not work and you will realize that you've forgotten to include one or more files. External dependencies don't need to go in your repo, but any file that you've authored should be included.
* Delete any temporary files or files that are no longer needed.
* Make sure there is no sensitive information (e.g. user names and passwords) in any files that will go in version control. It's best that your code reads these from a configuration file that is separate from your source code. This configuration file can then be excluded from your repo using a [.gitignore](https://help.github.com/articles/ignoring-files/) file. If you do this, then it can be helpful to others to create another file called something like config.TEMPLATE, with the exact same structure as your configure file, but without the sensitive information, and then include this in the repo. 
* Avoid putting binary files in your repo (databases, DLLs, compiled items etc). Again, use a [.gitignore](https://help.github.com/articles/ignoring-files/) file to exclude these.

##Source code in Riverscapes GitHub

Your source code should be stored in a git repository and uploaded into the [Riverscapes ](https://github.com/orgs/Riverscapes/dashboard) organization on GitHub. If you're new to GitHub, the default is to upload repositories under the umbrella of your own user account, so it's important that you understand how to upload the repo under riverscapes.

You should learn and understand how to use git first! Certainly research any of the terms below that are not readily obvious to you. But, at a high level, starting from a folder of non-version controlled source code on your computer, the steps are:

1. Install git version control software. 
2. Initialize a new git repo in your top level source code folder.
3. Commit all changes to the git repo.
4. Login to [GitHub](http://github.com)
5. Navigate to the [Riverscapes organization](https://github.com/orgs/Riverscapes/dashboard).
6. Click the green New Repository Button and fill in the necessary fields.
7. Copy the SSH address that GitHub provides once the repo is created.
8. On your local system, add a new **Remote**. Call it `origin` and paste the SSH address.
9. Push your source code up to origin.
10. Refresh the repo page on GitHub and verify that your source code appears.

## Read Me File

Add a file to the root (top level folder) of your repo called `readme.md` The `md` suffix tells GitHub that this is a plain text [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) document. It's important because GitHub renders this readme file below the listing of source code. See the [bottom of the PyBRAT repo](https://github.com/Riverscapes/pyBRAT) for an example.

Learn [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) if you don't know it already. You're going to be writing a lot of it!

For now, simply put one or two sentences in the read me that provide a high level overview of your model. You will be adding more info later...

## License File

Create and a plain text file in the root of your repository simply called LICENSE (no file suffix). [Choose an appropriate license](https://choosealicense.com/) and put the text in this file. Most of the Riverscapes models use the [GNU 3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Documentation Site







