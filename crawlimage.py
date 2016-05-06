# This program is heavily influenced and almost copied from http://code.activestate.com/recipes/577385-image-downloader/ 

import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup # for HTML parsing

global urlList
urlList = []

# recursively download images starting from the root URL
def downloadImages(url, level): # the root URL is level 0
    print url
    global urlList
    if url in urlList: # prevent using the same URL again
        return
    urlList.append(url)
    try:
        urlContent = urllib2.urlopen(url).read()
    except:
        return

    soup = BeautifulSoup(''.join(urlContent))
    # find and download all images
    imgTags = soup.findAll('img')
    for imgTag in imgTags:
        imgUrl = imgTag['src']
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = basename(urlsplit(imgUrl)[2])
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
        except:
            pass

    # if there are links on the webpage then recursively repeat
    if level > 0:
        linkTags = soup.findAll('a')
        if len(linkTags) > 0:
            for linkTag in linkTags:
                try:
                    linkUrl = linkTag['href']
                    downloadImages(linkUrl, level - 1)
                except:
                    pass

# main
downloadImages('http://www.yahoo.com', 0)
