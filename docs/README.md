# NARDocs Wiki


## Working locally

To get the latest theme:

```
bundle update
```

To autobuild the site locally

```
bundle exec jekyll serve
```

### Folder layout

Some special folders:

* `_site`: You may or may not see this. It is the compiled site on your local and should be ".gitignored".
* `assets`: this is where images, fonts, javascript and compiled CSS lives. Don't ever change CSS code here since it gets overwritten.
* `src`: This is where the page layouts, uncompiled CSS and everything "code-y" lives. If you're writing content just ignore this completely.

Some special files:

* `_config.yml` This is the configuration for your site. it tells Jekyll what the site name is, what flavour of markdown to use and what the default template is.
