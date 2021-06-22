# Mochaccino
**End To End Testing Framework**

## Mission
**To create a open source test tool for modern web applications while inlcuding best practices in testing without restrictions. At the same time keeping the framework flexible to extend and to include newer technologies with less friction.**

## Planned tech-stack
* Python
* [fastcore](https://fastcore.fast.ai/)
* [Playwright](https://playwright.dev/)

## Motivation behind starting this project
I have used selenium as part of my day job for front end testing and pytest as well. Recently I have started to fiddle around Cypress and was thoroughly impressed by it. However, Cypress doesn't support Python yet and has some design restrcitions of it's own(which is not necessarily a bad thing at all). Selenium on the other hand doesn't have the restrictions of Cypress (like no support for super domain in cypress) but it does come with some limitations of it's own which are mostly due to some bad choices made during the implementation of the selenium API by the end user.

My motive was to have a test tool which would have the nice user experience and modern API of Cypress and also the familiarity of Selenium's pyhton API. Currently the number of test tools which check all these requirements are less so this project is my effort to build an additional choice of a modern test tool for the test and devlopement communtiy and also somethign which I can use for my tetsing activities.
