# What is data parsing?
Data parsing is a process during which a piece of data gets converted into a different type of data according to specified criteria. It’s an important part of web scraping since it helps transform raw HTML data into a more easily readable format that can be understood and analyzed.

## What does a parser do?
A well-built parser will identify the needed HTML string and the relevant information within it. Based on predefined criteria and the rules of the parser, it’ll filter and combine the needed information into CSV, JSON, or any other format.


## What is Beautiful Soup?
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed web pages based on specific criteria that can be used to extract, navigate, search, and modify data from HTML, which is mostly used for web scraping. Beautiful Soup 4 is supported on Python versions 3.6 and greater. Being a useful library, it can save programmers loads of time when collecting data and parsing it.

## 1. Install the Beautiful Soup library
On Windows, when installing Python, make sure to tick the PATH installation checkbox. PATH installation adds executables to the default OS Command Prompt executable search. The OS will then recognize commands like `pip` or `python` without having to point to the directory of the executable, which makes things more convenient.

The next step is to install the Beautiful Soup 4 library on your system. No matter the OS, you can easily do it by using this command on the terminal to install the latest version of Beautiful Soup:

```bash
  pip install beautifulsoup4
```
