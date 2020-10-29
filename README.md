# Software and Systems Laboratory (SSL) Website

[![Build Status](https://travis-ci.org/LoyolaChicagoCS/ssl.svg)](https://travis-ci.org/LoyolaChicagoCS/ssl) ![Code Style](https://img.shields.io/badge/code%20style-black-black) [![LINK](https://img.shields.io/badge/link-ssl.cs.luc.edu-maroon)](https://ssl.cs.luc.edu)

## About

This is the repository behind the [SSL](https://ssl.cs.luc.edu) web site at Loyola University Chicago.

## Site Generation and Releases

Our site uses the [Sphinx] backend and generates automatically per commit with [Travis CI].

In addition, we release PDF and EPUB versions of the site per commit as well.

## Tips for the Maintainer

1. The [Sphinx docs] is not the best source out there for all of the features that [ReStructuredText] has to offer. Please reference the documents listed under [Documentation Links] for more information.

2. Use the [Black code formatter]. This does nothing but make Python code look pretty.

3. Become familiar with the [Travis CI docs] and [Travis-Sphinx docs] when writing `.travis.yml` files. More often than not, Travis CI and Travis-Sphinx will be the cause of most of your issues.

4. Write templates for all of the **TYPES** of webpages that are being created and keep them organized.

## Documentation Links

| Tool             | Documentation Link                                                 |
|------------------|--------------------------------------------------------------------|
| Black            | https://github.com/psf/black                                       |
| ReStructuredText | https://docutils.sourceforge.io/docs/ref/rst/definitions.html      |
|                  | https://docutils.sourceforge.io/docs/ref/rst/directives.html       |
|                  | https://docutils.sourceforge.io/docs/ref/rst/introduction.html     |
|                  | https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html |
|                  | https://docutils.sourceforge.io/docs/ref/rst/roles.html            |
| Sphinx           | https://www.sphinx-doc.org/en/master/contents.html                 |
| Travis CI        | https://docs.travis-ci.com/                                        |
| Travis-Sphinx    | https://github.com/syntaf/travis-sphinx                            |

[Sphinx]: https://www.sphinx-doc.org/en/master/index.html#
[Sphinx docs]: https://www.sphinx-doc.org/en/master/contents.html
[ReStructuredText]: https://docutils.sourceforge.io/docs/ref/rst/introduction.html
[Documentation Links]: #documentation-links
[Black code formatter]: https://github.com/psf/black
[Travis CI docs]: https://docs.travis-ci.com/
[Travis-Sphinx docs]: https://github.com/syntaf/travis-sphinx
