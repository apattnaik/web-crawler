# web-crawler
A simple web crawler using BeautifulSoup module in Python

A) crawl.py is a menu driven simple crawler which crawls a single webpage and returns
1. All the data in the file
2. All the links present
3. All the images present

Change the website name under the variable "url" or "fish_url" as required.

B) crawlimage.py downloads all the images in the website recursively, i.e., it downloads all the images in the webpage and finds all the links in that particular page and visits them to download images.

In the function call downloadImages(), any URL can be set in the first parameter and the second parameter may be set to 0 for downloading images of the given webpage and any value greater than 0 to download images recursively in the given website.
