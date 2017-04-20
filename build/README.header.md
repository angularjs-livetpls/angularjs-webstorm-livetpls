## Introduction

This repository contains LiveTemplates for [AngularJS](http://angularjs.org/) and [Jasmine](https://github.com/pivotal/jasmine) to be used with [JetBrains](http://www.jetbrains.com/) products such as [IntelliJ](http://www.jetbrains.com/idea/) or [WebStorm](http://www.jetbrains.com/webstorm/). Live Templates are a set of abbreviations that expand in to 'code snippets' for common tasks such as creating variables and functions. These abbreviations significantly speed up development and reduce coding errors.

Check out the [blog post](http://pkozlowskios.wordpress.com/2012/07/15/live-templates-for-angular-js-in-webstorm/) for more!

## Installation

### IntelliJ
Copy the Live Template xml files into your user's IntelliJ folder. This is typically in `[home directory]/.IntelliJIdea<version>/config/templates`. If IntelliJ is currently open, you will need to restart the IDE.

Note: The default Live Template expansion character is TAB. To use a Live Template abbreviation, type the abbreviation and press the expansion character. The Live Template definitions can be found in the Settings Menu (CTRL+ALT+S), IDE Settings, Live Templates, angular.js.

### WebStorm
AFAIK WebStorm doesn't have any particular installation (or import) procedure for LiveTemplates.
Instead just drop `*.xml` files from this repository into WebStorm's folder where it stores LiveTemplates.
Usually this is the `[your home directory]/.WebIde40/config/templates`.

## How to use the Live Templates
The following show the available abbrivations and their default implementations. Variables that are editable upon template expansion are delemited with the $ sign (ex. `$filterName$`).
`$END$` indicates where the cursor will be placed upon template completion.

